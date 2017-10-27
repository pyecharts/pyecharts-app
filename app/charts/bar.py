import random

from pyecharts import Bar, Page, Style
from app.charts.constants import WIDTH, HEIGHT


def create_charts():
    page = Page()

    style = Style(
        width=WIDTH, height=HEIGHT
    )

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    chart = Bar("柱状图-数据堆叠", **style.init_style)
    chart.add("商家A", attr, v1, is_stack=True)
    chart.add("商家B", attr, v2, is_stack=True, is_more_utils=True)
    page.add(chart)

    chart = Bar("柱状图-数据标记", **style.init_style)
    chart.add("商家A", attr, v1, mark_point=["average"])
    chart.add("商家B", attr, v2, mark_line=["min", "max"], is_more_utils=True)
    page.add(chart)

    chart = Bar("柱状图-xy 轴互换", **style.init_style)
    chart.add("商家A", attr, v1)
    chart.add("商家B", attr, v2, is_convert=True)
    page.add(chart)

    chart = Bar("柱状图-直方图", **style.init_style)
    chart.add("", attr * 2, v1 + v2, bar_category_gap=0)
    page.add(chart)

    attr = ["{}天".format(i) for i in range(20)]
    v1 = [random.randint(1, 20) for _ in range(20)]
    chart = Bar("柱状图-标签旋转", **style.init_style)
    chart.add("", attr, v1, xaxis_interval=0, xaxis_rotate=30,
              yaxis_rotate=30)
    page.add(chart)

    attr = ["{}月".format(i) for i in range(1, 8)]
    v1 = [0, 100, 200, 300, 400, 220, 250]
    v2 = [1000, 800, 600, 500, 450, 400, 300]
    chart = Bar("柱状图-瀑布图", **style.init_style)
    chart.add("", attr, v1, label_color=['rgba(0,0,0,0)'], is_stack=True)
    chart.add("月份", attr, v2, is_label_show=True, is_stack=True,
              label_pos='inside')
    page.add(chart)

    attr = ["{}月".format(i) for i in range(1, 13)]
    v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7,
          135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7,
          175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    chart = Bar("柱状图-数据缩放(slider)", **style.init_style)
    chart.add("蒸发量", attr, v1, mark_line=["average"],
              mark_point=["max", "min"])
    chart.add("降水量", attr, v2, mark_line=["average"],
              mark_point=["max", "min"],
              is_datazoom_show=True, datazoom_range=[50, 80])
    page.add(chart)

    attr = ["{}天".format(i) for i in range(30)]
    v1 = [random.randint(1, 30) for _ in range(30)]
    chart = Bar("柱状图-数据缩放(slider)", **style.init_style)
    chart.add("", attr, v1, is_label_show=True, is_datazoom_show=True)
    page.add(chart)

    attr = ["{}月".format(i) for i in range(1, 13)]
    v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    chart = Bar("柱状图-数据缩放(inside)", **style.init_style)
    chart.add("蒸发量", attr, v1, mark_line=["average"],
              mark_point=["max", "min"])
    chart.add("降水量", attr, v2, mark_line=["average"],
              mark_point=["max", "min"], is_datazoom_show=True,
              datazoom_range=[20, 60], datazoom_type='inside')
    page.add(chart)

    attr = ["{}天".format(i) for i in range(30)]
    v1 = [random.randint(1, 30) for _ in range(30)]
    chart = Bar("柱状图-数据缩放(inside)", **style.init_style)
    chart.add("", attr, v1, is_datazoom_show=True, datazoom_type='inside',
              datazoom_range=[10, 60])
    page.add(chart)

    attr = ["{}天".format(i) for i in range(30)]
    v1 = [random.randint(1, 30) for _ in range(30)]
    chart = Bar("柱状图-数据缩放(both)", **style.init_style)
    chart.add("", attr, v1, is_datazoom_show=True, datazoom_type='both',
              datazoom_range=[10, 60])
    page.add(chart)

    return page
