import random
import math

from pyecharts import Polar, Page, Style
from app.charts.constants import WIDTH, HEIGHT


def create_charts():
    page = Page()

    style = Style(
        width=WIDTH, height=HEIGHT
    )

    data = [(i, random.randint(1, 100)) for i in range(101)]
    chart = Polar("极坐标系-散点图", **style.init_style)
    chart.add("", data, boundary_gap=False, type='scatter',
              is_splitline_show=False, is_axisline_show=True)
    page.add(chart)

    data_1 = [(10, random.randint(1, 100)) for _ in range(300)]
    data_2 = [(11, random.randint(1, 100)) for _ in range(300)]
    chart = Polar("极坐标系-散点图", **style.init_style)
    chart.add("", data_1, type='scatter')
    chart.add("", data_2, type='scatter')
    page.add(chart)

    data = [(i, random.randint(1, 100)) for i in range(10)]
    chart = Polar("极坐标系-动态散点图", **style.init_style)
    chart.add("", data, type='effectScatter', effect_scale=10,
              effect_period=5)
    page.add(chart)

    radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    chart = Polar("极坐标系-堆叠柱状图", **style.init_style)
    _style1 = style.add(
        type="barRadius", is_stack=True
    )
    chart.add("A", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, **_style1)
    chart.add("B", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, **_style1)
    chart.add("C", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, **_style1)
    page.add(chart)

    radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    chart = Polar("极坐标系-堆叠柱状图", **style.init_style)
    _style2 = style.add(
        type="barAngle", is_stack=True
    )
    chart.add("", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, **_style2)
    chart.add("", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, **_style2)
    chart.add("", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, **_style2)
    page.add(chart)

    data = []
    for i in range(101):
        theta = i / 100 * 360
        r = 5 * (1 + math.sin(theta / 180 * math.pi))
        data.append([r, theta])
    hour = [i for i in range(1, 25)]
    chart = Polar("极坐标系-画爱心", **style.init_style)
    chart.add("Love", data, angle_data=hour, boundary_gap=False, start_angle=0)
    page.add(chart)

    data = []
    for i in range(361):
        t = i / 180 * math.pi
        r = math.sin(2 * t) * math.cos(2 * t)
        data.append([r, i])
    chart = Polar("极坐标系-画小花", **style.init_style)
    chart.add("Flower", data, start_angle=0, symbol=None, axis_range=[0, None])
    page.add(chart)

    data = []
    for i in range(361):
        t = i / 180 * math.pi
        r = math.sin(2 * t) * math.cos(2 * t)
        data.append([r, i])
    chart = Polar("极坐标系-画红色小花", **style.init_style)
    chart.add("Color-Flower", data, start_angle=0, symbol=None,
              axis_range=[0, None], area_color="#f71f24", area_opacity=0.6)
    page.add(chart)

    data = []
    for i in range(5):
        for j in range(101):
            theta = j / 100 * 360
            alpha = i * 360 + theta
            r = math.pow(math.e, 0.003 * alpha)
            data.append([r, theta])
    chart = Polar("极坐标系-画蜗牛", **style.init_style)
    chart.add("", data, symbol_size=0, symbol='circle', start_angle=-25,
              is_radiusaxis_show=False, area_color="#f3c5b3",
              area_opacity=0.5, is_angleaxis_show=False)
    page.add(chart)

    return page
