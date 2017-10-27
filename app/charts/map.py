from pyecharts import Map, Page, Style


def create_charts():
    page = Page()

    style = Style(
        width=1100, height=600
    )

    value = [155, 10, 66, 78]
    attr = ["福建", "山东", "北京", "上海"]
    chart = Map("全国地图", **style.init_style)
    chart.add("", attr, value, maptype='china', is_label_show=True)
    page.add(chart)

    value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
    attr = ["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
    chart = Map("全国地图-视觉通道", **style.init_style)
    chart.add("", attr, value, maptype='china', is_visualmap=True,
              visual_text_color='#000')
    page.add(chart)

    value = [20, 190, 253, 77, 65]
    attr = ['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市']
    chart = Map("广东地图", **style.init_style)
    chart.add("", attr, value, maptype='广东',
              is_visualmap=True, visual_text_color='#000')
    page.add(chart)

    value = [95.1, 23.2, 43.3, 66.4, 88.5, 0.1]
    attr = ["China", "Canada", "Brazil", "Russia",
            "United States", "Unknown Country"]
    chart = Map("世界地图 - 带标记点", **style.init_style)
    chart.add("", attr, value, maptype="world", is_visualmap=True,
              visual_text_color='#000')
    page.add(chart)

    chart = Map("世界地图 - 不带标记点", **style.init_style)
    chart.add("", attr, value, maptype="world", is_visualmap=True,
              is_map_symbol_show=False, visual_text_color='#000')
    page.add(chart)

    return page
