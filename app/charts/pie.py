import random

from pyecharts import Pie, Page
from .constants import WIDTH, HEIGHT


def pie_charts():
    page = Page()

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [11, 12, 13, 10, 10, 10]
    chart1 = Pie("饼图示例", width=WIDTH, height=HEIGHT)
    chart1.add("", attr, v1, is_label_show=True)
    page.add(chart1)

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [11, 12, 13, 10, 10, 10]
    chart2 = Pie("饼图-圆环图示例", title_pos='center', width=WIDTH, height=HEIGHT)
    chart2.add("", attr, v1, radius=[40, 75], label_text_color=None, is_label_show=True,
               legend_orient='vertical', legend_pos='left')
    page.add(chart2)

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [11, 12, 13, 10, 10, 10]
    v2 = [19, 21, 32, 20, 20, 33]
    chart3 = Pie("饼图-玫瑰图示例", title_pos='center', width=WIDTH, height=HEIGHT)
    chart3.add("商品A", attr, v1, center=[25, 50], is_random=True,
               radius=[30, 75], rosetype='radius')
    chart3.add("商品B", attr, v2, center=[75, 50], is_random=True,
               radius=[30, 75], rosetype='area',
               is_legend_show=False, is_label_show=True)
    page.add(chart3)

    chart4 = Pie("饼图示例", title_pos='center', width=WIDTH, height=HEIGHT)
    chart4.add("", ['A', 'B', 'C', 'D', 'E', 'F'], [335, 321, 234, 135, 251, 148],
               radius=[40, 55], is_label_show=True)
    chart4.add("", ['H', 'I', 'J'], [335, 679, 204], radius=[0, 30],
               legend_orient='vertical', legend_pos='left')
    page.add(chart4)

    attr = ['A', 'B', 'C', 'D', 'E', 'F']
    chart5 = Pie("饼图示例", width=WIDTH, height=HEIGHT)
    chart5.add("", attr, [random.randint(0, 100) for _ in range(6)], radius=[50, 55],
               center=[25, 50], is_random=True)
    chart5.add("", attr, [random.randint(20, 100) for _ in range(6)], radius=[0, 45],
               center=[25, 50], rosetype='area')
    chart5.add("", attr, [random.randint(0, 100) for _ in range(6)], radius=[50, 55],
               center=[65, 50], is_random=True)
    chart5.add("", attr, [random.randint(20, 100) for _ in range(6)], radius=[0, 45],
               center=[65, 50], rosetype='radius')
    page.add(chart5)

    chart6 = Pie('各类电影中"好片"所占的比例', "数据来着豆瓣",
                 title_pos='center', width=WIDTH, height=HEIGHT)
    chart6.add("", ["剧情", ""], [25, 75], center=[10, 30], radius=[18, 24],
               label_pos='center', is_label_show=True, label_text_color=None, )
    chart6.add("", ["奇幻", ""], [24, 76], center=[30, 30], radius=[18, 24],
               label_pos='center', is_label_show=True, label_text_color=None,
               legend_pos='left')
    chart6.add("", ["爱情", ""], [14, 86], center=[50, 30], radius=[18, 24],
               label_pos='center', is_label_show=True, label_text_color=None)
    chart6.add("", ["惊悚", ""], [11, 89], center=[70, 30], radius=[18, 24],
               label_pos='center', is_label_show=True, label_text_color=None)
    chart6.add("", ["冒险", ""], [27, 73], center=[90, 30], radius=[18, 24],
               label_pos='center', is_label_show=True, label_text_color=None)
    chart6.add("", ["动作", ""], [15, 85], center=[10, 70], radius=[18, 24],
               label_pos='center', is_label_show=True, label_text_color=None)
    chart6.add("", ["喜剧", ""], [54, 46], center=[30, 70], radius=[18, 24],
               label_pos='center', is_label_show=True, label_text_color=None)
    chart6.add("", ["科幻", ""], [26, 74], center=[50, 70], radius=[18, 24],
               label_pos='center', is_label_show=True, label_text_color=None)
    chart6.add("", ["悬疑", ""], [25, 75], center=[70, 70], radius=[18, 24],
               label_pos='center', is_label_show=True, label_text_color=None)
    chart6.add("", ["犯罪", ""], [28, 72], center=[90, 70], radius=[18, 24],
               label_pos='center', is_label_show=True, label_text_color=None,
               is_legend_show=True, legend_top="center")
    page.add(chart6)

    return page
