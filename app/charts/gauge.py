from pyecharts import Gauge, Page


def gauge_charts():
    page = Page()

    chart1 = Gauge("仪表盘示例")
    chart1.add("业务指标", "完成率", 66.66)
    page.add(chart1)

    chart2 = Gauge("仪表盘示例")
    chart2.add("业务指标", "完成率", 166.66, angle_range=[180, 0],
               scale_range=[0, 200], is_legend_show=False)
    page.add(chart2)

    return page
