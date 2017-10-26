import random

from pyecharts import Scatter3D, Page
from app.charts.constants import RANGE_COLOR, WIDTH, HEIGHT


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
