import random

from pyecharts import HeatMap, Page
from app.charts.constants import X_TIME, Y_WEEK, WIDTH, HEIGHT


def create_charts():
    page = Page()

    data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    chart = HeatMap("热力图示例", width=WIDTH, height=HEIGHT)
    chart.add("热力图直角坐标系", X_TIME, Y_WEEK, data, is_visualmap=True,
              visual_text_color="#000", visual_orient='horizontal')
    page.add(chart)

    import datetime
    begin = datetime.date(2017, 1, 1)
    end = datetime.date(2017, 12, 31)
    data = [[str(begin + datetime.timedelta(days=i)),
             random.randint(1000, 25000)] for i in range((end - begin).days + 1)]
    chart = HeatMap("日历热力图示例", "某人 2017 年微信步数情况", width=WIDTH)
    chart.add("", data, is_calendar_heatmap=True,
              visual_text_color='#000', visual_range_text=['', ''],
              visual_range=[1000, 25000], calendar_cell_size=['auto', 30],
              is_visualmap=True, calendar_date_range="2017",
              visual_orient="horizontal", visual_pos="center",
              visual_top="80%", is_piecewise=True)
    page.add(chart)

    return page
