from pyecharts import Funnel, Page
from .constants import WIDTH, HEIGHT


def funnel_charts():
    page = Page()

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    value = [20, 40, 60, 80, 100, 120]
    chart1 = Funnel("漏斗图示例", width=WIDTH, height=HEIGHT)
    chart1.add("商品", attr, value, is_label_show=True, label_pos="inside",
               label_text_color="#fff")
    page.add(chart1)

    chart2 = Funnel("漏斗图示例", width=WIDTH, height=HEIGHT, title_pos='center')
    chart2.add("商品", attr, value, is_label_show=True, label_pos="outside",
               legend_orient='vertical', legend_pos='left')
    page.add(chart2)

    return page
