from pyecharts import Map, Page


def map_charts():
    page = Page()

    value = [155, 10, 66, 78]
    attr = ["福建", "山东", "北京", "上海"]
    chart = Map("全国地图", width=1200, height=600)
    chart.add("", attr, value, maptype='china', is_label_show=True)
    page.add(chart)

    value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
    attr = ["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
    chart = Map("地图-VisualMap", width=1200, height=600)
    chart.add("", attr, value, maptype='china', is_visualmap=True,
              visual_text_color='#000')
    page.add(chart)

    value = [20, 190, 253, 77, 65]
    attr = ['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市']
    chart = Map("广东地图", width=1200, height=600)
    chart.add("", attr, value, maptype='广东',
              is_visualmap=True, visual_text_color='#000')
    page.add(chart)

    value = [95.1, 23.2, 43.3, 66.4, 88.5, 0.1]
    attr = [
        "China", "Canada", "Brazil", "Russia", "United States", "Unknown Country"
    ]
    chart = Map("世界地图", width=1200, height=600)
    chart.add("", attr, value, maptype="world", is_visualmap=True,
              visual_text_color='#000')
    page.add(chart)

    value = [155, 10, 66, 78]
    attr = ["福建", "山东", "北京", "上海"]
    chart = Map("全国地图", width=1200, height=600)
    chart.add("", attr, value, maptype='china')
    page.add(chart)

    return page
