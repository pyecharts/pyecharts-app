from pyecharts import Gauge, Page

WIDTH = 1100
HEIGHT = 550


def create_charts():
    page = Page()

    chart_init = {
        "width": WIDTH,
        "height": HEIGHT,
    }

    chart = Gauge("仪表盘示例", **chart_init)
    chart.add("业务指标", "完成率", 66.66)
    page.add(chart)

    chart = Gauge("仪表盘示例", **chart_init)
    chart.add("业务指标", "完成率", 166.66, angle_range=[180, 0],
              scale_range=[0, 200], is_legend_show=False)
    page.add(chart)

    return page
