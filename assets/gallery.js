(() => {
  const photo = (slug, file, layout, title, caption) => {
    const id = file.replace(/\.jpg$/, "");
    return {
      src: `assets/gallery/${slug}/${file}`,
      layout,
      title,
      caption,
      detailUrl: `gallery-${slug}-${id.replace(`${slug}-`, "")}.html`,
    };
  };

  window.BAR_GALLERY_GROUPS = [
    {
      id: "bar-233",
      title: "Bar 233",
      type: "酒吧",
      note: "一只蓝色杯子先落座，夜色才慢慢坐到它旁边。",
      tags: ["酒吧", "夜色", "吧台"],
      photos: [
        photo("bar-233", "bar-233-01.jpg", "tall", "吧台上的蓝", "蓝色酒液停在杯中，背后的瓶影和木色吧台一起把这一刻收暗。"),
      ],
    },
    {
      id: "qifei",
      title: "起飞",
      type: "旅途",
      note: "机翼、云层和蓝色窗光，是离开地面时最安静的部分。",
      tags: ["旅途", "云层", "起飞"],
      photos: [
        photo("qifei", "qifei-01.jpg", "tall", "云层下的机翼", "窗外只剩蓝色、云和一截机翼，城市被留在看不见的地方。"),
        photo("qifei", "qifei-02.jpg", "wide", "一片蓝色窗景", "云层铺得很低，机翼从画面边缘伸出去，像把旅途轻轻翻开。"),
        photo("qifei", "qifei-03.jpg", "tall", "贴着云的航线", "机翼掠过成片云层，蓝色把声音都滤得很远。"),
      ],
    },
    {
      id: "zoominn",
      title: "Zoom inN",
      type: "酒吧",
      note: "杯垫、玻璃和吧台灯，把 Zoom inN 留成几张冷静的近景。",
      tags: ["酒吧", "Zoom inN", "杯子"],
      photos: [
        photo("zoominn", "zoominn-01.jpg", "tall", "泡沫停在杯口", "杯子立在圆形杯垫上，泡沫细细铺开，吧台的光在背后低着。"),
        photo("zoominn", "zoominn-02.jpg", "tall", "倒入杯中的光", "细流落进杯中，玻璃边缘被灯照亮，动作比人声更清楚。"),
        photo("zoominn", "zoominn-03.jpg", "tall", "吧台前的一次倾倒", "调酒的手势停在半明半暗里，水线和杯口形成很轻的一条弧。"),
        photo("zoominn", "zoominn-04.jpg", "tall", "空杯的轮廓", "一只三角杯站在吧台前，透明得几乎只剩杯壁和背后的光。"),
        photo("zoominn", "zoominn-05.jpg", "tall", "透明三角杯", "高脚杯安静立着，杯面还没有被填满，像一个刚开始的夜晚。"),
      ],
    },
    {
      id: "sober-company-2",
      title: "Sober Company（二代）",
      type: "酒吧",
      note: "这一组不急着说明什么，只把杯子在暗处亮起来的瞬间留下。",
      tags: ["酒吧", "Sober Company", "二代", "杯子"],
      photos: [
        photo("sober-company-2", "sober-company-2-01.jpg", "tall", "暗处的琥珀", "一杯深色酒靠在画面边缘，灯从后面过来，只照亮杯中的一点琥珀。"),
        photo("sober-company-2", "sober-company-2-02.jpg", "tall", "红色小杯", "红色酒液在暗处显得很轻，旁边的黄色纸签像一枚小小的注脚。"),
        photo("sober-company-2", "sober-company-2-03.jpg", "tall", "三角杯的侧光", "玻璃杯被一条暖光勾出轮廓，液面安静地停在中间。"),
        photo("sober-company-2", "sober-company-2-04.jpg", "tall", "两只杯子的背影", "两只杯子站在暗处，背后的灯带很亮，像把夜晚隔在更远的地方。"),
        photo("sober-company-2", "sober-company-2-05.jpg", "tall", "杯中的红", "红色酒液被泡沫托住，玻璃和灯光都退到它身后。"),
        photo("sober-company-2", "sober-company-2-06.jpg", "tall", "圆杯里的沉静", "杯中有一枚深色轮廓，液面平得像刚刚把一句话说完。"),
        photo("sober-company-2", "sober-company-2-07.jpg", "tall", "远处的瓶影", "杯子和瓶影被放在很深的暗处，吧台只留下几处反光。"),
        photo("sober-company-2", "sober-company-2-08.jpg", "tall", "调酒的手", "手、瓶口和杯子挤在暖光里，动作正好停在倒下去之前。"),
        photo("sober-company-2", "sober-company-2-09.jpg", "tall", "红杯前的手势", "红色杯子在吧台上亮着，人的手势把画面带出一点正在发生的速度。"),
        photo("sober-company-2", "sober-company-2-10.jpg", "tall", "薄泡与绿叶", "浅色酒液上覆着一层薄泡，一片绿叶把暗色吧台轻轻提亮。"),
        photo("sober-company-2", "sober-company-2-11.jpg", "tall", "紫色渐层", "紫色从杯底往上晕开，像暗处突然亮出的一小段晚风。"),
      ],
    },
    {
      id: "pony-up",
      title: "Pony Up",
      type: "餐酒",
      note: "窗边的杯子和餐桌上的颜色，让白天也有一点微醺。",
      tags: ["餐酒", "窗边", "餐桌"],
      photos: [
        photo("pony-up", "pony-up-01.jpg", "tall", "窗边的白酒", "白酒杯贴着窗光，街上的颜色虚虚地映进来，午后也变得慢了一点。"),
        photo("pony-up", "pony-up-02.jpg", "tall", "红绿之间", "一盘颜色很满的食物摆在桌上，红和绿几乎要从画面里跳出来。"),
        photo("pony-up", "pony-up-03.jpg", "tall", "杯垫上的橙色", "一杯橙色饮品靠着窗边，玻璃、杯垫和街景刚好分成三层。"),
      ],
    },
    {
      id: "bar-blanc",
      title: "Bar Blanc",
      type: "酒吧",
      note: "杯子在吧台前各自站好，颜色很轻，光也很轻。",
      tags: ["酒吧", "吧台", "杯子"],
      photos: [
        photo("bar-blanc", "bar-blanc-01.jpg", "wide", "薄荷立起来", "黄色长杯放在吧台前，薄荷叶往上伸，背后的酒瓶被光虚化。"),
        photo("bar-blanc", "bar-blanc-02.jpg", "tall", "一杯黄色的夜", "同一只杯子被竖着留下，冰块、薄荷和黄色酒液都更靠近眼前。"),
        photo("bar-blanc", "bar-blanc-03.jpg", "tall", "绿意短杯", "浅绿色短杯站在杯垫上，玻璃里有一点雾气，也有一点安静。"),
        photo("bar-blanc", "bar-blanc-04.jpg", "tall", "粉色长杯", "粉色长饮在灯下显得很清亮，杯口的装饰像给夜晚别上的一枚小签。"),
        photo("bar-blanc", "bar-blanc-06.jpg", "tall", "橙粉色杯影", "橙粉色酒液靠在暗木桌面上，水杯在旁边分走一点光。"),
        photo("bar-blanc", "bar-blanc-07.jpg", "tall", "浅色短杯", "浅色酒液停在厚底杯里，杯壁和冰块把光折得很软。"),
      ],
    },
    {
      id: "italian-restaurant",
      title: "某意大利餐厅",
      type: "餐厅",
      note: "名字先空着，盘子里的热气和颜色已经足够把那顿饭记住。",
      tags: ["餐厅", "餐桌", "晚餐"],
      photos: [
        photo("italian-restaurant", "italian-restaurant-01.jpg", "wide", "火腿与芝麻菜", "披萨铺满火腿、芝麻菜和芝士碎，像把一顿饭最热闹的部分先端上来。"),
        photo("italian-restaurant", "italian-restaurant-02.jpg", "wide", "橙黄色意面", "意面卷在橙黄色酱汁里，叉子停在旁边，画面像刚刚开动。"),
        photo("italian-restaurant", "italian-restaurant-03.jpg", "wide", "海鲜意面", "贝壳和虾藏在酱汁之间，白盘边缘留着一圈温柔的亮。"),
        photo("italian-restaurant", "italian-restaurant-04.jpg", "wide", "奶油宽面", "宽面叠在白盘中央，奶油色把整张照片都放软了。"),
        photo("italian-restaurant", "italian-restaurant-05.jpg", "wide", "炸物与红酱", "炸物切在盘中，红色酱汁拖出一笔，让这一盘显得利落又热。"),
      ],
    },
    {
      id: "dorm-1108",
      title: "出去吃饭的合照",
      type: "聚餐",
      note: "不是宿舍，是几次出去吃饭时顺手留下的人和桌子。",
      tags: ["聚餐", "合照", "餐桌"],
      photos: [
        photo("dorm-1108", "dorm-1108-01.jpg", "wide", "热气里的合照", "一桌菜和几个人挤在同一个画面里，照片不求整齐，只求当时都在。"),
        photo("dorm-1108", "dorm-1108-02.jpg", "wide", "饭后的站定", "几个人靠近镜头，杯子和招牌一起入画，像把散场前的一秒按住。"),
        photo("dorm-1108", "dorm-1108-03.jpg", "wide", "披萨旁的碰杯", "桌上有披萨、酒瓶和伸来的手，热闹没有摆好姿势就被留下了。"),
        photo("dorm-1108", "dorm-1108-04.jpg", "tall", "冰柜前的碰杯", "几只手在冰柜前碰到一起，饮料罐和玻璃门把这一刻照得很亮。"),
      ],
    },
  ];
})();
