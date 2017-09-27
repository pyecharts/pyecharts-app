from pyecharts import Map, Page


def map_charts():
    page = Page()

    value = [155, 10, 66, 78]
    attr = ["福建", "山东", "北京", "上海"]
    chart1 = Map("全国地图示例", width=1200, height=600)
    chart1.add("", attr, value, maptype='china', is_label_show=True)
    page.add(chart1)

    value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
    attr = ["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
    chart2 = Map("Map 结合 VisualMap 示例", width=1200, height=600)
    chart2.add("", attr, value, maptype='china', is_visualmap=True,
               visual_text_color='#000')
    page.add(chart2)

    value = [20, 190, 253, 77, 65]
    attr = ['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市']
    chart3 = Map("广东地图示例", width=1200, height=600)
    chart3.add("", attr, value, maptype='广东',
               is_visualmap=True, visual_text_color='#000')
    page.add(chart3)

    value = [95.1, 23.2, 43.3, 66.4, 88.5, 0.1]
    attr = [
        "China", "Canada", "Brazil", "Russia", "United States", "Unknown Country"
    ]
    chart4 = Map("世界地图示例", width=1200, height=600)
    chart4.add("", attr, value, maptype="world", is_visualmap=True,
               visual_text_color='#000')
    page.add(chart4)

    value = [155, 10, 66, 78]
    attr = ["福建", "山东", "北京", "上海"]
    chart5 = Map("全国地图示例", width=1200, height=600)
    chart5.add("", attr, value, maptype='china')
    page.add(chart5)

    return page
