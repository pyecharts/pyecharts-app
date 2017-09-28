from pyecharts import Gauge, Page


def gauge_charts():
    page = Page()

    chart = Gauge("仪表盘示例")
    chart.add("业务指标", "完成率", 66.66)
    page.add(chart)

    chart = Gauge("仪表盘示例")
    chart.add("业务指标", "完成率", 166.66, angle_range=[180, 0],
              scale_range=[0, 200], is_legend_show=False)
    page.add(chart)

    return page
