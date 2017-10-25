import random

from pyecharts import Scatter3D, Page

RANGE_COLOR = ['#313695', '#4575b4', '#74add1', '#abd9e9',
               '#e0f3f8', '#ffffbf', '#fee090', '#fdae61',
               '#f46d43', '#d73027', '#a50026']

WIDTH = 1100
HEIGHT = 550


def create_charts():
    page = Page()

    data = [
        [random.randint(0, 100),
         random.randint(0, 100),
         random.randint(0, 100)] for _ in range(80)
    ]
    chart = Scatter3D("3D 散点图", width=WIDTH, height=HEIGHT)
    chart.add("", data, is_visualmap=True, visual_range_color=RANGE_COLOR)
    page.add(chart)

    return page
