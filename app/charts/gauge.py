from pyecharts import Gauge, Page, Style
from app.charts.constants import HEIGHT, WIDTH


def create_charts():
    page = Page()

    style = Style(
        width=WIDTH, height=HEIGHT
    )
    chart = Gauge("仪表盘示例", **style.init_style)
    chart.add("业务指标", "完成率", 66.66)
    page.add(chart)

    chart = Gauge("仪表盘示例", **style.init_style)
    chart.add("业务指标", "完成率", 166.66, angle_range=[180, 0],
              scale_range=[0, 200], is_legend_show=False)
    page.add(chart)

    return page
