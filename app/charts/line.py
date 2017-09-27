import random
import math

from pyecharts import Line, Page
from .constants import WIDTH, HEIGHT


def line_charts():
    page = Page()

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 10, 100]
    v2 = [55, 60, 16, 20, 15, 80]
    chart1 = Line("折线图-默认标记", width=WIDTH, height=HEIGHT)
    chart1.add("商家A", attr, v1, mark_point=["average"])
    chart1.add("商家B", attr, v2, is_smooth=True, mark_line=["max", "average"])
    page.add(chart1)

    chart2 = Line("折线图-自定义标记", width=WIDTH, height=HEIGHT)
    chart2.add("商家A", attr, v1,
               mark_point=["average", {
                   "coord": ["裤子", 10], "name": "这是我想要的第一个标记点"}])
    chart2.add("商家B", attr, v2, is_smooth=True,
               mark_point=[{
                   "coord": ["袜子", 80], "name": "这是我想要的第二个标记点"}])
    page.add(chart2)

    chart3 = Line("折线图-标记图标", width=WIDTH, height=HEIGHT)
    chart3.add("商家A", attr, v1, mark_point=["average", "max", "min"],
               mark_point_symbol='diamond', mark_point_textcolor='#40ff27')
    chart3.add("商家B", attr, v2, mark_point=["average", "max", "min"],
               mark_point_symbol='arrow', mark_point_symbolsize=40)
    page.add(chart3)

    attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    chart4 = Line("折线图-某地气温", width=WIDTH, height=HEIGHT)
    chart4.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10],
               mark_point=["max", "min"], mark_line=["average"])
    chart4.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0],
               mark_point=["max", "min"], mark_line=["average"])
    page.add(chart4)

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 10, 100]
    v2 = [55, 60, 16, 20, 15, 80]
    chart5 = Line("折线图-数据堆叠", width=WIDTH, height=HEIGHT)
    chart5.add("商家A", attr, v1, is_stack=True, is_label_show=True)
    chart5.add("商家B", attr, v2, is_stack=True, is_label_show=True)
    page.add(chart5)

    chart6 = Line("折线图-阶梯图", width=WIDTH, height=HEIGHT)
    chart6.add("商家A", attr, v1, is_step=True, is_label_show=True)
    page.add(chart6)

    chart7 = Line("折线图-面积图", width=WIDTH, height=HEIGHT)
    chart7.add("商家A", attr, v1, is_fill=True, line_opacity=0.2,
               area_opacity=0.4, symbol=None)
    chart7.add("商家B", attr, v2, is_fill=True, area_color='#000',
               area_opacity=0.3, is_smooth=True)
    page.add(chart7)

    chart8 = Line("折线图-对数坐标轴", width=WIDTH, height=HEIGHT)
    chart8.add("商家A", attr, [math.log10(random.randint(1, 99999)) for _ in range(6)])
    chart8.add("商家B", attr, [math.log10(random.randint(1, 99999999)) for _ in range(6)],
               yaxis_type="log")
    page.add(chart8)

    return page
