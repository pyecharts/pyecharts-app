import random
import math

from pyecharts import Line, Page, Style
from app.charts.constants import WIDTH, HEIGHT


def create_charts():
    page = Page()

    style = Style(
        width=WIDTH, height=HEIGHT
    )

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 10, 100]
    v2 = [55, 60, 16, 20, 15, 80]
    chart = Line("折线图-默认标记", **style.init_style)
    chart.add("商家A", attr, v1, mark_point=["average"])
    chart.add("商家B", attr, v2, is_smooth=True,
              mark_line=["max", "average"], is_more_utils=True)
    page.add(chart)

    chart = Line("折线图-自定义标记", **style.init_style)
    chart.add("商家A", attr, v1,
              mark_point=["average", {
                  "coord": ["裤子", 10], "name": "这是我想要的第一个标记点"}])
    chart.add("商家B", attr, v2, is_smooth=True, is_more_utils=True,
              mark_point=[{
                  "coord": ["袜子", 80], "name": "这是我想要的第二个标记点"}])
    page.add(chart)

    chart = Line("折线图-标记图标", **style.init_style)
    chart.add("商家A", attr, v1, mark_point=["average", "max", "min"],
              mark_point_symbol='diamond', mark_point_textcolor='#40ff27')
    chart.add("商家B", attr, v2, mark_point=["average", "max", "min"],
              mark_point_symbol='arrow', mark_point_symbolsize=40)
    page.add(chart)

    attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    chart = Line("折线图-某地气温", **style.init_style)
    chart.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10],
              mark_point=["max", "min"], mark_line=["average"])
    chart.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0],
              mark_point=["max", "min"], mark_line=["average"])
    page.add(chart)

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 10, 100]
    v2 = [55, 60, 16, 20, 15, 80]
    chart = Line("折线图-数据堆叠", **style.init_style)
    chart.add("商家A", attr, v1, is_stack=True, is_label_show=True)
    chart.add("商家B", attr, v2, is_stack=True, is_label_show=True)
    page.add(chart)

    chart = Line("折线图-阶梯图", **style.init_style)
    chart.add("商家A", attr, v1, is_step=True, is_label_show=True)
    page.add(chart)

    chart = Line("折线图-面积图", **style.init_style)
    chart.add("商家A", attr, v1, is_fill=True, line_opacity=0.2,
              area_opacity=0.4, symbol=None)
    chart.add("商家B", attr, v2, is_fill=True, area_color='#000',
              area_opacity=0.3, is_smooth=True)
    page.add(chart)

    chart = Line("折线图-对数坐标轴", width=WIDTH, height=HEIGHT)
    chart.add("商家A", attr,
              [math.log10(random.randint(1, 99999)) for _ in range(6)])
    chart.add("商家B", attr,
              [math.log10(random.randint(1, 99999999)) for _ in range(6)],
              yaxis_type="log")
    page.add(chart)

    return page
