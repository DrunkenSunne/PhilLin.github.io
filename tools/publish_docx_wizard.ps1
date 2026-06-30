param(
  [switch]$Help
)

$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$publisher = Join-Path $scriptDir "publish_docx.ps1"

function Show-Help {
  Write-Host ""
  Write-Host "Phil Lin Bar Word publishing wizard"
  Write-Host ""
  Write-Host "Run:"
  Write-Host "  powershell -ExecutionPolicy Bypass -File .\tools\publish_docx_wizard.ps1"
  Write-Host ""
  Write-Host "This wizard asks for:"
  Write-Host "  1. Word .docx path"
  Write-Host "  2. note or article"
  Write-Host "  3. optional title, summary, slug, date, mood"
  Write-Host "  4. preview"
  Write-Host "  5. final confirmation"
  Write-Host ""
}

function Read-Required($prompt) {
  while ($true) {
    $value = Read-Host $prompt
    if (-not [string]::IsNullOrWhiteSpace($value)) {
      return $value.Trim()
    }
    Write-Host "This cannot be empty. Please try again." -ForegroundColor Yellow
  }
}

function Read-Optional($prompt) {
  $value = Read-Host $prompt
  if ([string]::IsNullOrWhiteSpace($value)) {
    return ""
  }
  return $value.Trim()
}

function Read-Choice($prompt, [string[]]$validValues, $defaultValue) {
  while ($true) {
    $suffix = if ($defaultValue) { " [default: $defaultValue]" } else { "" }
    $value = Read-Host "$prompt$suffix"
    if ([string]::IsNullOrWhiteSpace($value) -and $defaultValue) {
      return $defaultValue
    }
    $value = $value.Trim()
    if ($validValues -contains $value) {
      return $value
    }
    Write-Host "Please enter: $($validValues -join ' / ')" -ForegroundColor Yellow
  }
}

function Normalize-PathInput($value) {
  $path = $value.Trim()
  if ($path.StartsWith('& ')) {
    $path = $path.Substring(2).Trim()
  }
  $path = $path.Trim('"').Trim("'")
  return $path
}

function Add-OptionalArg([System.Collections.Generic.List[string]]$argsList, $name, $value) {
  if (-not [string]::IsNullOrWhiteSpace($value)) {
    $argsList.Add($name)
    $argsList.Add($value)
  }
}

function Invoke-Publisher([string[]]$publisherArgs) {
  & powershell -ExecutionPolicy Bypass -File $publisher @publisherArgs
  return $LASTEXITCODE
}

if ($Help) {
  Show-Help
  exit 0
}

Show-Help
Write-Host "Start. Press Enter for anything you are not sure about." -ForegroundColor Cyan
Write-Host ""

if (-not (Test-Path $publisher)) {
  Write-Host "Publisher script not found: $publisher" -ForegroundColor Red
  exit 1
}

while ($true) {
  Write-Host "Step 1: Word file path." -ForegroundColor Cyan
  Write-Host "Tip: drag the .docx file into this terminal window, then press Enter."
  $docxInput = Read-Required "Word .docx path"
  $docxPath = Normalize-PathInput $docxInput

  if (-not (Test-Path -LiteralPath $docxPath)) {
    Write-Host "File not found: $docxPath" -ForegroundColor Yellow
    Write-Host "Check the path and try again."
    continue
  }

  if ([System.IO.Path]::GetExtension($docxPath).ToLowerInvariant() -ne ".docx") {
    Write-Host "This does not look like a .docx file: $docxPath" -ForegroundColor Yellow
    $continueAnyway = Read-Choice "Continue anyway? Enter y or n" @("y", "n") "n"
    if ($continueAnyway -ne "y") {
      continue
    }
  }

  break
}

Write-Host ""
Write-Host "Step 2: Choose publish type." -ForegroundColor Cyan
Write-Host "1 = bar note, generates note-*.html"
Write-Host "2 = full article, generates article-*.html"
$kindChoice = Read-Choice "Enter 1 or 2" @("1", "2") "1"
$kind = if ($kindChoice -eq "2") { "article" } else { "note" }

$tag = ""
$mood = ""
if ($kind -eq "article") {
  Write-Host ""
  Write-Host "Step 3: Choose article category." -ForegroundColor Cyan
  Write-Host "1 = life log"
  Write-Host "2 = thoughts"
  Write-Host "3 = recommendations"
  Write-Host "4 = type manually"
  $tagChoice = Read-Choice "Enter 1 / 2 / 3 / 4" @("1", "2", "3", "4") "1"
  switch ($tagChoice) {
    "1" { $tag = "生活日志" }
    "2" { $tag = "一些思绪" }
    "3" { $tag = "种草安利" }
    "4" { $tag = Read-Required "Type category name" }
  }
} else {
  $tag = "吧台札记"
  Write-Host ""
  Write-Host "Step 3: Optional mood word for the note." -ForegroundColor Cyan
  Write-Host "Leave empty to use the default."
  $mood = Read-Optional "Mood"
}

Write-Host ""
Write-Host "Step 4: Optional fields." -ForegroundColor Cyan
Write-Host "Leave empty if you are not sure. The script can infer title and summary."
$title = Read-Optional "Title"
$summary = Read-Optional "Summary"
$slug = Read-Optional "English slug, for example rainy-review-day"
$date = Read-Optional "Publish date, for example 2026-06-30"

$info = ""
if ($kind -eq "article") {
  $info = Read-Optional "Article info"
}
$endnote = Read-Optional "End note"

$argsList = [System.Collections.Generic.List[string]]::new()
$argsList.Add($docxPath)
$argsList.Add("--kind")
$argsList.Add($kind)
Add-OptionalArg $argsList "--tag" $tag
Add-OptionalArg $argsList "--mood" $mood
Add-OptionalArg $argsList "--title" $title
Add-OptionalArg $argsList "--summary" $summary
Add-OptionalArg $argsList "--slug" $slug
Add-OptionalArg $argsList "--date" $date
Add-OptionalArg $argsList "--info" $info
Add-OptionalArg $argsList "--endnote" $endnote

Write-Host ""
Write-Host "Step 5: Preview first." -ForegroundColor Cyan
Write-Host "Preview does not write files."
$previewChoice = Read-Choice "Preview now? Enter y or n" @("y", "n") "y"
if ($previewChoice -eq "y") {
  $previewArgs = [System.Collections.Generic.List[string]]::new()
  foreach ($item in $argsList) {
    $previewArgs.Add($item)
  }
  $previewArgs.Add("--dry-run")
  $exitCode = Invoke-Publisher $previewArgs.ToArray()
  if ($exitCode -ne 0) {
    Write-Host ""
    Write-Host "Preview failed. Do not publish yet. Check the error above." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit $exitCode
  }
}

Write-Host ""
Write-Host "Step 6: Final confirmation." -ForegroundColor Cyan
Write-Host "Publishing will edit files in this repo."
$publishChoice = Read-Choice "Publish now? Enter y or n" @("y", "n") "n"
if ($publishChoice -ne "y") {
  Write-Host "Canceled. Nothing was published." -ForegroundColor Yellow
  Read-Host "Press Enter to exit"
  exit 0
}

$exitCode = Invoke-Publisher $argsList.ToArray()
if ($exitCode -eq 0) {
  Write-Host ""
  Write-Host "Published." -ForegroundColor Green
  Write-Host "Recommended checks:"
  Write-Host "  node --check assets/content.js"
  Write-Host "  git status --short"
  Write-Host "  git diff --stat"
} else {
  Write-Host ""
  Write-Host "Publish failed. Check the error above." -ForegroundColor Red
}

Read-Host "Press Enter to exit"
exit $exitCode
