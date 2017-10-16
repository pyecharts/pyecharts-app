from pyecharts import TreeMap, Page
from .constants import HEIGHT, WIDTH, TREEMAP


def treemap_charts():
    data = [
        {
            "value": 40,
            "name": "我是A",
        },
        {
            "value": 180,
            "name": "我是B",
            "children": [
                {
                    "value": 76,
                    "name": "我是B.children",
                    "children": [
                        {
                            "value": 12,
                            "name": "我是B.children.a",
                        },
                        {
                            "value": 28,
                            "name": "我是B.children.b",
                        },
                        {
                            "value": 20,
                            "name": "我是B.children.c",
                        },
                        {
                            "value": 16,
                            "name": "我是B.children.d",
                        }]
                }]}
    ]

    page = Page()
    chart = TreeMap("树图-默认示例", width=WIDTH, height=HEIGHT)
    chart.add("演示数据", data, is_label_show=True, label_pos='inside')
    page.add(chart)

    chart = TreeMap("树图-下钻示例", width=WIDTH, height=HEIGHT)
    chart.add("演示数据", data, is_label_show=True, label_pos='inside',
              treemap_left_depth=1)
    page.add(chart)

    chart = TreeMap("树图-官方示例", width=WIDTH, height=HEIGHT)
    chart.add("演示数据", TREEMAP, is_label_show=True, label_pos='inside')
    page.add(chart)

    return page
