import random

from pyecharts import HeatMap, Page
from .constants import X_TIME, Y_WEEK, WIDTH, HEIGHT


def heatmap_charts():
    page = Page()

    data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    chart = HeatMap("热力图示例", width=WIDTH, height=HEIGHT)
    chart.add("热力图直角坐标系", X_TIME, Y_WEEK, data, is_visualmap=True,
              visual_text_color="#000", visual_orient='horizontal')
    page.add(chart)

    return page
