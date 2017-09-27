import random

from pyecharts import Bar, Page
from .constants import WIDTH, HEIGHT


def bar_charts():
    page = Page()

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    chart1 = Bar("柱状图数据堆叠示例", width=WIDTH, height=HEIGHT)
    chart1.add("商家A", attr, v1, is_stack=True)
    chart1.add("商家B", attr, v2, is_stack=True)
    page.add(chart1)

    chart2 = Bar("标记线和标记点示例", width=WIDTH, height=HEIGHT)
    chart2.add("商家A", attr, v1, mark_point=["average"])
    chart2.add("商家B", attr, v2, mark_line=["min", "max"])
    page.add(chart2)

    chart3 = Bar("x 轴和 y 轴交换", width=WIDTH, height=HEIGHT)
    chart3.add("商家A", attr, v1)
    chart3.add("商家B", attr, v2, is_convert=True)
    page.add(chart3)

    attr = ["{}天".format(i) for i in range(20)]
    v1 = [random.randint(1, 20) for _ in range(20)]
    chart4 = Bar("坐标轴标签旋转示例", width=WIDTH, height=HEIGHT)
    chart4.add("", attr, v1, xaxis_interval=0, xaxis_rotate=30,
               yaxis_rotate=30)
    page.add(chart4)

    attr = ["{}月".format(i) for i in range(1, 8)]
    v1 = [0, 100, 200, 300, 400, 220, 250]
    v2 = [1000, 800, 600, 500, 450, 400, 300]
    chart5 = Bar("瀑布图示例", width=WIDTH, height=HEIGHT)
    chart5.add("", attr, v1, label_color=['rgba(0,0,0,0)'], is_stack=True)
    chart5.add("月份", attr, v2, is_label_show=True, is_stack=True,
               label_pos='inside')
    page.add(chart5)

    attr = ["{}月".format(i) for i in range(1, 13)]
    v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7,
          135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7,
          175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    chart6 = Bar("Bar - dataZoom - slider 示例", width=WIDTH, height=HEIGHT)
    chart6.add("蒸发量", attr, v1, mark_line=["average"], mark_point=["max", "min"])
    chart6.add("降水量", attr, v2, mark_line=["average"], mark_point=["max", "min"],
               is_datazoom_show=True, datazoom_range=[50, 80])
    page.add(chart6)

    attr = ["{}天".format(i) for i in range(30)]
    v1 = [random.randint(1, 30) for _ in range(30)]
    chart7 = Bar("Bar - dataZoom - slider 示例", width=WIDTH, height=HEIGHT)
    chart7.add("", attr, v1, is_label_show=True, is_datazoom_show=True)
    page.add(chart7)

    attr = ["{}月".format(i) for i in range(1, 13)]
    v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    chart8 = Bar("Bar - dataZoom - inside 示例", width=1000, height=500)
    chart8.add("蒸发量", attr, v1, mark_line=["average"], mark_point=["max", "min"])
    chart8.add("降水量", attr, v2, mark_line=["average"], mark_point=["max", "min"],
               is_datazoom_show=True, datazoom_range=[20, 60], datazoom_type='inside')
    page.add(chart8)

    attr = ["{}天".format(i) for i in range(30)]
    v1 = [random.randint(1, 30) for _ in range(30)]
    chart9 = Bar("Bar - dataZoom - inside 示例", width=WIDTH, height=HEIGHT)
    chart9.add("", attr, v1, is_datazoom_show=True, datazoom_type='inside',
               datazoom_range=[10, 25])
    page.add(chart9)

    return page
