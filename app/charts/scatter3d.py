import random

from pyecharts import Scatter3D, Page
from .constants import RANGE_COLOR, WIDTH, HEIGHT


def scatter3d_charts():
    page = Page()

    data = [
        [random.randint(0, 100),
         random.randint(0, 100),
         random.randint(0, 100)] for _ in range(80)
    ]
    chart1 = Scatter3D("3D 散点图", width=WIDTH, height=HEIGHT)
    chart1.add("", data, is_visualmap=True, visual_range_color=RANGE_COLOR)
    page.add(chart1)

    return page
