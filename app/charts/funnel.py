from pyecharts import Funnel, Page, Style
from app.charts.constants import WIDTH, HEIGHT


def create_charts():
    page = Page()

    style = Style(
        width=WIDTH, height=HEIGHT
    )

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    value = [20, 40, 60, 80, 100, 120]
    chart = Funnel("漏斗图示例", **style.init_style)
    chart.add("商品", attr, value, is_label_show=True, label_pos="inside",
              label_text_color="#fff")
    page.add(chart)

    chart = Funnel("漏斗图示例", title_pos='center', **style.init_style)
    chart.add("商品", attr, value, is_label_show=True, label_pos="outside",
              legend_orient='vertical', legend_pos='left')
    page.add(chart)

    return page
