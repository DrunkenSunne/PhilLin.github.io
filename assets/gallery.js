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
      note: "吧台、低光和第一张落下来的夜晚。",
      tags: ["酒吧", "夜色", "吧台"],
      photos: [
        photo("bar-233", "bar-233-01.jpg", "tall", "蓝色杯影", "一杯蓝色酒躺在木色吧台上，杯脚和桌面反光把夜晚压得很低。"),
      ],
    },
    {
      id: "qifei",
      title: "起飞",
      type: "旅途",
      note: "飞机窗外的蓝色云层，像一小段离开地面的开场。",
      tags: ["旅途", "云层", "起飞"],
      photos: [
        photo("qifei", "qifei-01.jpg", "tall", "云层和机翼", "机翼贴着一大片蓝色云层，像刚把城市留在身后。"),
        photo("qifei", "qifei-02.jpg", "wide", "窗外的蓝", "云和天都被机窗滤成冷蓝色，中间留出一点飞行时的安静。"),
        photo("qifei", "qifei-03.jpg", "tall", "贴近云面的航线", "机翼从画面下方伸出去，云层像一块缓慢移动的地面。"),
      ],
    },
    {
      id: "zoominn",
      title: "ZOOMINN",
      type: "酒吧",
      note: "杯子、桌面和 ZOOMINN 的一点冷色调。",
      tags: ["酒吧", "ZOOMINN", "杯子"],
      photos: [
        photo("zoominn", "zoominn-01.jpg", "tall", "杯脚上的圆形杯垫", "一只泡沫细密的杯子站在圆形杯垫上，吧台后面的金属和玻璃都收进暗处。"),
        photo("zoominn", "zoominn-02.jpg", "tall", "器具旁的斜光", "金属器具和玻璃杯贴着吧台排开，光从一侧擦过去。"),
        photo("zoominn", "zoominn-03.jpg", "tall", "吧台设备的侧影", "设备和杯具被压进窄窄的纵向画面里，像一段正在准备中的动作。"),
        photo("zoominn", "zoominn-04.jpg", "tall", "玻璃和金属的近景", "杯壁、管线和金属边缘在暗处重叠，留下很冷的一层反光。"),
        photo("zoominn", "zoominn-05.jpg", "tall", "空杯和吧台", "一只细脚杯站在吧台中央，杯身几乎透明，后面的人影把现场感留住。"),
      ],
    },
    {
      id: "sober-company-2",
      title: "Sober Company（二代）",
      type: "酒吧",
      note: "这一组更像连续镜头：从杯壁、低光到调酒动作。",
      tags: ["酒吧", "Sober Company", "二代", "杯子"],
      photos: [
        photo("sober-company-2", "sober-company-2-01.jpg", "tall", "暗处的琥珀色", "一只酒杯在暖光里靠近画面边缘，背景被压成很深的黑。"),
        photo("sober-company-2", "sober-company-2-02.jpg", "tall", "红色小杯", "红色酒液和高脚杯在暗处亮起来，像吧台上一个小小的标点。"),
        photo("sober-company-2", "sober-company-2-03.jpg", "tall", "透明杯壁", "杯壁被暖光勾出轮廓，旁边的玻璃和阴影都在慢慢退后。"),
        photo("sober-company-2", "sober-company-2-04.jpg", "tall", "两只杯子的低光", "两只酒杯并排站着，背后的灯带把酒液照出一点琥珀色。"),
        photo("sober-company-2", "sober-company-2-05.jpg", "tall", "红色酒面", "杯中红色酒液被暗光托起来，整个画面像只剩下杯口和影子。"),
        photo("sober-company-2", "sober-company-2-06.jpg", "tall", "三角杯的轮廓", "一只三角杯在吧台灯下变得很清楚，酒面安静地停在中间。"),
        photo("sober-company-2", "sober-company-2-07.jpg", "tall", "远处的吧台", "杯子退到画面一侧，远处的灯和瓶影把空间拉长。"),
        photo("sober-company-2", "sober-company-2-08.jpg", "tall", "调酒中的手", "调酒动作被拍在半暗的吧台前，手、杯子和瓶标都带着一点速度。"),
        photo("sober-company-2", "sober-company-2-09.jpg", "tall", "调酒动作的下一拍", "手上的动作还没结束，红色酒液和吧台光线一起晃了一下。"),
        photo("sober-company-2", "sober-company-2-10.jpg", "tall", "白色泡沫杯", "一杯浅色饮品放在杯垫上，泡沫和小装饰把画面提亮。"),
        photo("sober-company-2", "sober-company-2-11.jpg", "tall", "紫色酒杯", "紫色酒液在细脚杯里透亮起来，像暗处突然亮出的一个小灯。"),
      ],
    },
    {
      id: "pony-up",
      title: "Pony Up",
      type: "餐酒",
      note: "窗边的酒、餐桌上的辣椒和一点日间光。",
      tags: ["餐酒", "窗边", "餐桌"],
      photos: [
        photo("pony-up", "pony-up-01.jpg", "tall", "窗边白葡萄酒", "一杯白葡萄酒靠着窗边，外面的红绿灯光把白天也拍得有点像夜晚。"),
        photo("pony-up", "pony-up-02.jpg", "tall", "红绿辣椒的餐盘", "一盘颜色很响的食物放在桌上，红椒和青椒把画面推到最前面。"),
        photo("pony-up", "pony-up-03.jpg", "tall", "窗边啤酒", "一杯啤酒放在圆形杯垫上，窗外的街景和室内桌面刚好分成两层。"),
      ],
    },
    {
      id: "bar-blanc",
      title: "Bar Blanc",
      type: "酒吧",
      note: "吧台和杯子的边缘比较清楚，像一组安静的存档。",
      tags: ["酒吧", "吧台", "杯子"],
      photos: [
        photo("bar-blanc", "bar-blanc-01.jpg", "wide", "薄荷长饮", "一杯黄色长饮立在吧台前，薄荷叶和背后的酒瓶一起往上生长。"),
        photo("bar-blanc", "bar-blanc-02.jpg", "tall", "黄色杯身和薄荷", "杯身转成竖向后更像一张小肖像，黄色酒液和薄荷叶都很亮。"),
        photo("bar-blanc", "bar-blanc-03.jpg", "tall", "绿色短饮", "一只绿色短饮杯站在灯前，透明杯壁里有一层柔和的雾。"),
        photo("bar-blanc", "bar-blanc-04.jpg", "tall", "粉色长饮", "粉色长饮被吧台灯照得很干净，杯口的装饰像一个小旗子。"),
        photo("bar-blanc", "bar-blanc-06.jpg", "tall", "橙粉色长饮", "一杯橙粉色酒放在暗木桌面上，旁边的水杯把光线分成两层。"),
        photo("bar-blanc", "bar-blanc-07.jpg", "tall", "浅色短杯", "浅色泡沫停在杯口，杯子被压在吧台角落里，显得很安静。"),
      ],
    },
    {
      id: "italian-restaurant",
      title: "某意大利餐厅",
      type: "餐厅",
      note: "暂时不知道全名，就先按那顿饭的光线记下来。",
      tags: ["餐厅", "餐桌", "晚餐"],
      photos: [
        photo("italian-restaurant", "italian-restaurant-01.jpg", "wide", "火腿披萨", "火腿和芝麻菜铺在披萨上，白色芝士碎像撒在热气上的一点雪。"),
        photo("italian-restaurant", "italian-restaurant-02.jpg", "wide", "橙黄色意面", "一盘橙黄色意面占满画面，叉子停在旁边，像刚要开始吃。"),
        photo("italian-restaurant", "italian-restaurant-03.jpg", "wide", "海鲜意面", "贝壳和虾藏在奶油色酱汁里，盘子边缘留着一圈暖光。"),
        photo("italian-restaurant", "italian-restaurant-04.jpg", "wide", "奶油宽面", "奶油宽面卷在白盘中央，整体柔软得像一小团白色云。"),
        photo("italian-restaurant", "italian-restaurant-05.jpg", "wide", "炸物和红色酱汁", "炸物被切在盘子一侧，红色酱汁拖出一条很利落的线。"),
      ],
    },
    {
      id: "dorm-1108",
      title: "出去吃饭的合照",
      type: "聚餐",
      note: "一起出去吃饭时留下的合照和餐桌瞬间。",
      tags: ["聚餐", "合照", "餐桌"],
      photos: [
        photo("dorm-1108", "dorm-1108-01.jpg", "wide", "餐桌上的合照", "一桌人、几盘菜和挡住脸的贴纸一起挤进画面，热闹比构图更重要。"),
        photo("dorm-1108", "dorm-1108-02.jpg", "wide", "饭后合影", "几个人靠在一起举着杯子，背景里的招牌和贴纸让这张更像一张小纪念。"),
        photo("dorm-1108", "dorm-1108-03.jpg", "wide", "披萨和举杯", "桌上有披萨和酒瓶，手伸进画面碰到一起，是很直接的一次聚餐记录。"),
        photo("dorm-1108", "dorm-1108-04.jpg", "tall", "冰柜前的碰杯", "几只手在冰柜前举着瓶罐碰到一起，像散场前又多留了一秒。"),
      ],
    },
  ];
})();
