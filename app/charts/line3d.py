import math

from pyecharts import Line3D, Page

RANGE_COLOR = ['#313695', '#4575b4', '#74add1', '#abd9e9',
               '#e0f3f8', '#ffffbf', '#fee090', '#fdae61',
               '#f46d43', '#d73027', '#a50026']
WIDTH = 1100
HEIGHT = 550


def create_charts():
    page = Page()

    chart_init = {
        "width": WIDTH,
        "height": HEIGHT,
    }

    _data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        _data.append([x, y, z])
    chart = Line3D("3D 折线图-默认", **chart_init)
    chart.add("", _data, is_visualmap=True, visual_range_color=RANGE_COLOR,
              visual_range=[0, 30], grid3d_rotate_sensitivity=5)
    page.add(chart)

    _data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        _data.append([x, y, z])
    chart = Line3D("3D 折线图-自动旋转", **chart_init)
    chart.add("", _data, is_visualmap=True, visual_range_color=RANGE_COLOR,
              visual_range=[0, 30], is_grid3d_rotate=True,
              grid3d_rotate_speed=180)
    page.add(chart)

    return page
