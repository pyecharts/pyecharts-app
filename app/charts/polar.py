import random
import math

from pyecharts import Polar, Page
from .constants import WIDTH, HEIGHT


def polar_charts():
    page = Page()

    data = [(i, random.randint(1, 100)) for i in range(101)]
    chart1 = Polar("极坐标系-散点图示例", width=WIDTH, height=HEIGHT)
    chart1.add("", data, boundary_gap=False, type='scatter',
               is_splitline_show=False, is_axisline_show=True)
    page.add(chart1)

    data_1 = [(10, random.randint(1, 100)) for i in range(300)]
    data_2 = [(11, random.randint(1, 100)) for i in range(300)]
    chart2 = Polar("极坐标系-散点图示例", width=WIDTH, height=HEIGHT)
    chart2.add("", data_1, type='scatter')
    chart2.add("", data_2, type='scatter')
    page.add(chart2)

    data = [(i, random.randint(1, 100)) for i in range(10)]
    chart3 = Polar("极坐标系-动态散点图示例", width=WIDTH, height=HEIGHT)
    chart3.add("", data, type='effectScatter', effect_scale=10,
               effect_period=5)
    page.add(chart3)

    radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    chart4 = Polar("极坐标系-堆叠柱状图示例", width=WIDTH, height=HEIGHT)
    chart4.add("A", [1, 2, 3, 4, 3, 5, 1], radius_data=radius,
               type='barRadius', is_stack=True)
    chart4.add("B", [2, 4, 6, 1, 2, 3, 1], radius_data=radius,
               type='barRadius', is_stack=True)
    chart4.add("C", [1, 2, 3, 4, 1, 2, 5], radius_data=radius,
               type='barRadius', is_stack=True)
    page.add(chart4)

    radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    chart5 = Polar("极坐标系-堆叠柱状图示例", width=WIDTH, height=HEIGHT)
    chart5.add("", [1, 2, 3, 4, 3, 5, 1], radius_data=radius,
               type='barAngle', is_stack=True)
    chart5.add("", [2, 4, 6, 1, 2, 3, 1], radius_data=radius,
               type='barAngle', is_stack=True)
    chart5.add("", [1, 2, 3, 4, 1, 2, 5], radius_data=radius,
               type='barAngle', is_stack=True)
    page.add(chart5)

    data = []
    for i in range(101):
        theta = i / 100 * 360
        r = 5 * (1 + math.sin(theta / 180 * math.pi))
        data.append([r, theta])
    hour = [i for i in range(1, 25)]
    chart6 = Polar("极坐标系-画爱心", width=WIDTH, height=HEIGHT)
    chart6.add("Love", data, angle_data=hour, boundary_gap=False, start_angle=0)
    page.add(chart6)

    data = []
    for i in range(361):
        t = i / 180 * math.pi
        r = math.sin(2 * t) * math.cos(2 * t)
        data.append([r, i])
    chart7 = Polar("极坐标系-画小花", width=WIDTH, height=HEIGHT)
    chart7.add("Flower", data, start_angle=0, symbol=None, axis_range=[0, None])
    page.add(chart7)

    data = []
    for i in range(361):
        t = i / 180 * math.pi
        r = math.sin(2 * t) * math.cos(2 * t)
        data.append([r, i])
    chart8 = Polar("极坐标系-画红色小花", width=WIDTH, height=HEIGHT)
    chart8.add("Color-Flower", data, start_angle=0, symbol=None,
              axis_range=[0, None], area_color="#f71f24", area_opacity=0.6)
    page.add(chart8)

    data = []
    for i in range(5):
        for j in range(101):
            theta = j / 100 * 360
            alpha = i * 360 + theta
            r = math.pow(math.e, 0.003 * alpha)
            data.append([r, theta])
    chart9 = Polar("极坐标系-画蜗牛", width=WIDTH, height=HEIGHT)
    chart9.add("", data, symbol_size=0, symbol='circle', start_angle=-25,
               is_radiusaxis_show=False, area_color="#f3c5b3",
               area_opacity=0.5, is_angleaxis_show=False)
    page.add(chart9)

    return page
