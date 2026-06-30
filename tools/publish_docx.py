#!/usr/bin/env python3
"""Publish a Word .docx as a static Phil Lin Bar article or bar note.

This is intentionally dependency-free: it uses only the Python standard library
so Codex or the user can run it in the repo without installing a build system.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import sys
import unicodedata
import zipfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
CONTENT_JS = ROOT / "assets" / "content.js"

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}

C = {
    "brand": "Phil Lin\u7684Bar",
    "home": "\u9996\u9875",
    "posts": "\u6587\u7ae0",
    "tonight": "\u4eca\u665a",
    "places": "\u79c1\u85cf",
    "playlist": "\u6b4c\u5355",
    "gallery": "\u6444\u5f71",
    "about": "\u5173\u4e8e",
    "friends": "\u53cb\u94fe",
    "main_nav": "\u4e3b\u5bfc\u822a",
    "toggle": "\u5f00\u5173\u52a8\u6548\uff1a\u70db\u5149\u5fae\u7c92",
    "published": "\u53d1\u5e03\u65f6\u95f4",
    "note": "\u672d\u8bb0",
    "article_body": "\u6587\u7ae0\u6b63\u6587",
    "bar_note": "\u5427\u53f0\u672d\u8bb0",
    "life_log": "\u751f\u6d3b\u65e5\u5fd7",
    "thoughts": "\u4e00\u4e9b\u601d\u7eea",
    "recommendations": "\u79cd\u8349\u5b89\u5229",
    "article_tags": "\u6587\u7ae0\u6807\u7b7e",
    "article_info": "\u6587\u7ae0\u4fe1\u606f",
    "return_archive": "\u8fd4\u56de\u6587\u7ae0\u5f52\u6863",
    "return_posts": "\u8fd4\u56de\u5f52\u6863",
    "cup_note": "\u676f\u5e95\u6ce8\u91ca",
    "no_summary": "\u4e00\u7bc7\u4ece Word \u6587\u6863\u53d1\u5e03\u7684\u6587\u5b57\u3002",
    "note_info": "\u4e00\u7bc7\u4ece Word \u6587\u6863\u53d1\u5e03\u7684\u5427\u53f0\u672d\u8bb0\u3002",
    "article_info_fallback": "\u4e00\u7bc7\u4ece Word \u6587\u6863\u53d1\u5e03\u7684\u6587\u7ae0\u3002",
    "endnote": "\u6587\u5b57\u5df2\u7ecf\u843d\u676f\uff0c\u4eca\u5929\u5148\u5b58\u5230\u8fd9\u91cc\u3002",
    "visual_skipped": "Visual verification was skipped by project preference.",
}


@dataclass
class Block:
    text: str
    images: list[str]


@dataclass
class DocxContent:
    paragraphs: list[str]
    blocks: list[Block]
    media: dict[str, str]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def text_from_paragraph(para: ET.Element) -> str:
    parts: list[str] = []
    for node in para.iter():
        if node.tag == f"{{{NS['w']}}}t":
            parts.append(node.text or "")
        elif node.tag == f"{{{NS['w']}}}tab":
            parts.append("\t")
        elif node.tag == f"{{{NS['w']}}}br":
            parts.append("\n")
    return "".join(parts).strip()


def docx_relationships(zf: zipfile.ZipFile) -> dict[str, str]:
    rel_path = "word/_rels/document.xml.rels"
    if rel_path not in zf.namelist():
        return {}
    root = ET.fromstring(zf.read(rel_path))
    rels: dict[str, str] = {}
    for rel in root.findall("rel:Relationship", NS):
        rid = rel.attrib.get("Id")
        target = rel.attrib.get("Target", "")
        if rid and target:
            rels[rid] = "word/" + target.lstrip("/")
    return rels


def extract_docx(path: Path) -> DocxContent:
    with zipfile.ZipFile(path) as zf:
        rels = docx_relationships(zf)
        root = ET.fromstring(zf.read("word/document.xml"))
        blocks: list[Block] = []
        paragraphs: list[str] = []
        media: dict[str, str] = {}

        for para in root.findall(".//w:body/w:p", NS):
            text = text_from_paragraph(para)
            images: list[str] = []
            for blip in para.findall(".//a:blip", NS):
                rid = blip.attrib.get(f"{{{NS['r']}}}embed")
                if rid and rid in rels and rels[rid].startswith("word/media/"):
                    images.append(rid)
                    media[rid] = rels[rid]
            if text:
                paragraphs.append(text)
            if text or images:
                blocks.append(Block(text=text, images=images))
    return DocxContent(paragraphs=paragraphs, blocks=blocks, media=media)


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return value or f"post-{date.today():%Y%m%d}"


def make_summary(paragraphs: list[str], title: str, limit: int = 120) -> str:
    body = " ".join(p for p in paragraphs if p != title).strip()
    if not body:
        return C["no_summary"]
    summary = re.split(r"(?<=[。！？.!?])", body, maxsplit=2)[0].strip() or body
    if len(summary) > limit:
        summary = summary[:limit].rstrip() + "..."
    return summary


def js_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def metadata_object(fields: dict[str, str]) -> str:
    lines = ["  {"]
    for key, value in fields.items():
        lines.append(f"    {key}: {js_string(value)},")
    lines.append("  },")
    return "\n".join(lines)


def insert_metadata(kind: str, fields: dict[str, str], force: bool) -> None:
    text = read_text(CONTENT_JS)
    post_id = fields["id"]
    if re.search(rf'id:\s*{re.escape(js_string(post_id))}', text):
        if not force:
            raise SystemExit(f"Metadata id already exists: {post_id}. Use --force to continue.")
        text = re.sub(
            rf"\n  \{{\n(?:    .+\n)*?    id:\s*{re.escape(js_string(post_id))},\n(?:    .+\n)*?  \}},",
            "",
            text,
            count=1,
        )

    array_name = "BAR_NOTES" if kind == "note" else "BAR_POSTS"
    marker = f"window.{array_name} = [\n"
    if marker not in text:
        raise SystemExit(f"Could not find {marker.strip()} in assets/content.js")
    text = text.replace(marker, marker + metadata_object(fields) + "\n", 1)
    write_text(CONTENT_JS, text)


def refresh_asset_versions(version: str) -> int:
    count = 0
    pattern = re.compile(r"((?:\.\./)?assets/(?:styles\.css|content\.js|gripes\.js|site\.js|bar-badge\.png)\?v=)[^\"']+")
    for path in ROOT.rglob("*.html"):
        text = read_text(path)
        new_text, changed = pattern.subn(rf"\g<1>{version}", text)
        if changed:
            write_text(path, new_text)
            count += changed
    return count


def copy_media(docx: Path, content: DocxContent, slug: str) -> dict[str, str]:
    copied: dict[str, str] = {}
    if not content.media:
        return copied
    out_dir = ROOT / "assets" / "posts" / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(docx) as zf:
        for rid, internal in content.media.items():
            source_name = Path(internal).name
            dest = out_dir / source_name
            with zf.open(internal) as src, dest.open("wb") as dst:
                shutil.copyfileobj(src, dst)
            copied[rid] = f"assets/posts/{slug}/{source_name}"
    return copied


def render_body(blocks: Iterable[Block], image_paths: dict[str, str]) -> str:
    rendered: list[str] = []
    for block in blocks:
        if block.text:
            rendered.append(f"        <p>{html.escape(block.text).replace(chr(10), '<br>')}</p>")
        for rid in block.images:
            src = image_paths.get(rid)
            if src:
                rendered.append(
                    '        <figure class="article-figure">'
                    f'<img src="{html.escape(src)}" alt="">'
                    "</figure>"
                )
    return "\n\n".join(rendered)


def page_html(
    *,
    kind: str,
    title: str,
    summary: str,
    published: str,
    tag: str,
    mood: str,
    info: str,
    endnote: str,
    version: str,
    body: str,
) -> str:
    if kind == "note":
        main_class = "article-layout drink-page drink-hanky-panky"
        article_class = "article note-article"
        glyph_class = "hanky-panky-glyph"
        drink_label = f"Hanky Panky · {C['bar_note']}"
        eyebrow = "Bar Notes"
        meta_tail = C["note"]
    else:
        main_class = "article-layout drink-page drink-martini"
        article_class = "article"
        glyph_class = "martini-glyph"
        drink_label = f"Martini · {C['article_body']}"
        eyebrow = tag
        meta_tail = f"{C['posts']}\uff1a{tag}"

    return f"""<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(title)} | {C['brand']}</title>
    <meta name="description" content="{html.escape(summary)}">
    <link rel="stylesheet" href="assets/styles.css?v={version}">
    <style>
      .article-deck {{
        max-width: 44rem;
        color: var(--muted);
        font-size: 1rem;
        line-height: 1.9;
      }}
    </style>
  </head>
  <body>
    <header class="site-header">
      <a class="brand" href="index.html"><img class="brand-mark brand-badge" src="assets/bar-badge.png?v={version}" alt=""><span>{C['brand']}</span></a>
      <nav class="nav-links" aria-label="{C['main_nav']}">
        <a href="index.html">{C['home']}</a>
        <a href="posts.html" aria-current="page">{C['posts']}</a>
        <a href="tonight.html">{C['tonight']}</a>
        <a href="reviews.html">{C['places']}</a>
        <a href="playlist.html">{C['playlist']}</a>
        <a href="gallery.html">{C['gallery']}</a>
        <a href="about.html">{C['about']}</a>
      </nav>
      <button class="icon-button" id="themeToggle" type="button" aria-label="{C['toggle']}" title="{C['toggle']}">✦</button>
    </header>

    <main class="{main_class}">
      <article class="{article_class}">
        <header class="article-header">
          <div class="drink-portrait">
            <span class="drink-glyph {glyph_class}"><span></span></span>
            <span>{drink_label}</span>
          </div>
          <p class="eyebrow">{html.escape(eyebrow)}</p>
          <h1>{html.escape(title)}</h1>
          <p class="article-meta">{C['published']}：{published} · {html.escape(meta_tail)}</p>
          <p class="article-deck">{html.escape(summary)}</p>
        </header>

{body}

        <footer class="article-endnote">
          <p>{C['cup_note']}：{html.escape(endnote)}</p>
        </footer>
      </article>

      <aside class="article-aside">
        <div class="aside-block">
          <h2>{C['article_tags']}</h2>
          <div class="tag-row">
            <span>{html.escape(tag)}</span>
            <span>{html.escape(mood)}</span>
          </div>
        </div>
        <div class="aside-block">
          <h2>{C['article_info']}</h2>
          <p>{html.escape(info)}</p>
          <a class="button primary full" href="posts.html">{C['return_archive']}</a>
        </div>
      </aside>
    </main>

    <footer class="site-footer">
      <span>© {published[:4]} {C['brand']}</span>
      <span><a href="posts.html">{C['return_posts']}</a></span>
      <span class="footer-link"><a href="friends.html">{C['friends']}</a></span>
    </footer>

    <script src="assets/content.js?v={version}"></script>
    <script src="assets/gripes.js?v={version}"></script>
    <script src="assets/site.js?v={version}"></script>
  </body>
</html>
"""


def update_agent_files(
    *,
    kind: str,
    docx: Path,
    slug: str,
    title: str,
    tag: str,
    published: str,
    summary: str,
    url: str,
    version: str,
    media_count: int,
) -> None:
    today = date.today().isoformat()
    type_label = "bar note" if kind == "note" else "article"
    changelog_title = f"{published} Automated Word {type_label.title()} Published - {slug}"
    media_line = (
        f"- Extracted and copied {media_count} embedded media file(s)."
        if media_count
        else "- The Word document contained no embedded media files."
    )

    context = ROOT / "AGENT_CONTEXT.md"
    text = read_text(context)
    text = re.sub(r"Last updated: \d{4}-\d{2}-\d{2}", f"Last updated: {today}", text, count=1)
    insert = f"""
## {changelog_title}

- Published `{docx}` as `{url}` using `tools/publish_docx.py`.
- Kind: `{kind}`; tag: `{tag}`.
- Final title is `{title}`.
- Publication date is `{published}`.
- Summary is `{summary}`
- Metadata id is `{slug}` and the entry is indexed in `assets/content.js`.
{media_line}
- Current asset query string is `{version}`.
- Visual verification was skipped by project preference.

"""
    text = text.replace("\nThis file externalizes", "\nThis file externalizes", 1)
    marker_end = text.find("\n## ")
    marker_end = text.find("\n## ", marker_end + 1)
    if marker_end == -1:
        text += insert
    else:
        text = text[:marker_end] + "\n" + insert + text[marker_end:]
    write_text(context, text)

    todo = ROOT / "AGENT_TODO.md"
    text = read_text(todo)
    text = re.sub(r"Last updated: \d{4}-\d{2}-\d{2}", f"Last updated: {today}", text, count=1)
    item = f"""- [x] Published {published} automated Word {type_label} from `{docx}`:
  - Generated `{url}` with `tools/publish_docx.py`.
  - Added metadata id `{slug}` to `assets/content.js`.
  - Tag is `{tag}`.
  - Refreshed HTML asset query strings to `{version}`.
  - Visual verification skipped by project preference.
"""
    text = text.replace("## 3. Phase-Two Candidate Tasks\n\n", "## 3. Phase-Two Candidate Tasks\n\n" + item, 1)
    write_text(todo, text)

    changelog = ROOT / "AGENT_CHANGELOG.md"
    text = read_text(changelog)
    text = re.sub(r"Last updated: \d{4}-\d{2}-\d{2}", f"Last updated: {today}", text, count=1)
    section = f"""## {changelog_title}

User published `{docx}` through the automated Word publishing helper.

- Generated final static file `{url}`.
- Added metadata id `{slug}` to `assets/content.js`.
- Kind: `{kind}`; tag: `{tag}`.
- Final title: `{title}`.
- Final summary: `{summary}`
- Publication date: `{published}`.
{media_line}
- Refreshed HTML asset query strings to `{version}`.
- {C['visual_skipped']}
- Rollback: delete `{url}`, remove the `{slug}` entry from `assets/content.js`, restore the previous HTML asset query string from git, and remove this changelog/context/todo/handoff entry if reverting the publication.

"""
    text = text.replace("\n## ", "\n" + section + "## ", 1)
    write_text(changelog, text)

    handoff = ROOT / "AGENT_HANDOFF.md"
    text = read_text(handoff)
    text = re.sub(r"Last updated: \d{4}-\d{2}-\d{2}", f"Last updated: {today}", text, count=1)
    para = (
        f"{published} automated Word {type_label}: `{docx}` was published with "
        f"`tools/publish_docx.py` as `{url}`. Kind `{kind}`, tag `{tag}`, "
        f"title `{title}`, metadata id `{slug}`, asset query string `{version}`. "
        f"{media_line[2:]} {C['visual_skipped']}\n\n"
    )
    text = text.replace("\n\n", "\n\n" + para, 1)
    write_text(handoff, text)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("docx", type=Path)
    parser.add_argument("--kind", choices=["note", "article"], default="note")
    parser.add_argument("--slug")
    parser.add_argument("--title")
    parser.add_argument("--summary")
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--tag")
    parser.add_argument("--mood")
    parser.add_argument("--info")
    parser.add_argument("--endnote", default=C["endnote"])
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--no-cache-refresh", action="store_true")
    parser.add_argument("--no-agent-log", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    docx = args.docx.resolve()
    if not docx.exists():
        raise SystemExit(f"File not found: {docx}")

    content = extract_docx(docx)
    if not content.paragraphs and not content.media:
        raise SystemExit("No text or media found in document.")

    title = args.title or (content.paragraphs[0] if content.paragraphs else docx.stem)
    slug = args.slug or slugify(title)
    if args.kind == "note" and not slug.startswith("note-"):
        out_name = f"note-{slug}.html"
    elif args.kind == "article" and not slug.startswith("article-"):
        out_name = f"article-{slug}.html"
    else:
        out_name = f"{slug}.html"
    url = out_name
    slug_id = re.sub(r"^(note|article)-", "", Path(out_name).stem)
    out_path = ROOT / out_name
    if out_path.exists() and not args.force:
        raise SystemExit(f"Output already exists: {out_path}. Use --force to overwrite.")

    tag = args.tag or (C["bar_note"] if args.kind == "note" else C["life_log"])
    mood = args.mood or (C["note"] if args.kind == "note" else tag)
    summary = args.summary or make_summary(content.paragraphs[1:] or content.paragraphs, title)
    info = args.info or (C["note_info"] if args.kind == "note" else C["article_info_fallback"])
    version = f"bar-art-{args.date.replace('-', '')}-{slug_id}"

    image_paths = copy_media(docx, content, slug_id)
    body = render_body(content.blocks[1:] if content.paragraphs and content.paragraphs[0] == title else content.blocks, image_paths)
    html_text = page_html(
        kind=args.kind,
        title=title,
        summary=summary,
        published=args.date,
        tag=tag,
        mood=mood,
        info=info,
        endnote=args.endnote,
        version=version,
        body=body,
    )

    fields = {
        "id": slug_id,
        "title": title,
        "tag": tag,
        "publishedAt": args.date,
    }
    if args.kind == "note":
        fields["mood"] = mood
    fields["summary"] = summary
    fields["url"] = url

    if args.dry_run:
        print(json.dumps({"url": url, "id": slug_id, "version": version, "fields": fields}, ensure_ascii=False, indent=2))
        return 0

    write_text(out_path, html_text)
    insert_metadata(args.kind, fields, args.force)
    refreshed = 0 if args.no_cache_refresh else refresh_asset_versions(version)
    if not args.no_agent_log:
        update_agent_files(
            kind=args.kind,
            docx=docx,
            slug=slug_id,
            title=title,
            tag=tag,
            published=args.date,
            summary=summary,
            url=url,
            version=version,
            media_count=len(image_paths),
        )

    print(json.dumps({
        "created": url,
        "id": slug_id,
        "kind": args.kind,
        "tag": tag,
        "version": version,
        "media_count": len(image_paths),
        "refreshed_asset_refs": refreshed,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
