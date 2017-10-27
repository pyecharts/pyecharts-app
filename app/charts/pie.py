import random

from pyecharts import Pie, Page, Style
from app.charts.constants import WIDTH, HEIGHT


def create_charts():
    page = Page()

    style = Style(
        width=WIDTH, height=HEIGHT
    )

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [11, 12, 13, 10, 10, 10]
    chart = Pie("饼图示例", **style.init_style)
    chart.add("", attr, v1, is_label_show=True)
    page.add(chart)

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [11, 12, 13, 10, 10, 10]
    chart = Pie("饼图-圆环图示例", title_pos='center', **style.init_style)
    chart.add("", attr, v1, radius=[40, 75], label_text_color=None,
              is_label_show=True, legend_orient='vertical', legend_pos='left')
    page.add(chart)

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [11, 12, 13, 10, 10, 10]
    v2 = [19, 21, 32, 20, 20, 33]
    chart = Pie("饼图-玫瑰图示例", title_pos='center', **style.init_style)
    chart.add("商品A", attr, v1, center=[25, 50], is_random=True,
              radius=[30, 75], rosetype='radius')
    chart.add("商品B", attr, v2, center=[75, 50], is_random=True,
              radius=[30, 75], rosetype='area',
              is_legend_show=False, is_label_show=True)
    page.add(chart)

    chart = Pie("饼图示例", title_pos='center', **style.init_style)
    chart.add("", ['A', 'B', 'C', 'D', 'E', 'F'], [335, 321, 234, 135, 251, 148],
              radius=[40, 55], is_label_show=True)
    chart.add("", ['H', 'I', 'J'], [335, 679, 204], radius=[0, 30],
              legend_orient='vertical', legend_pos='left')
    page.add(chart)

    attr = ['A', 'B', 'C', 'D', 'E', 'F']
    chart = Pie("饼图示例", **style.init_style)
    chart.add("", attr, [random.randint(0, 100) for _ in range(6)],
              radius=[50, 55], center=[25, 50], is_random=True)
    chart.add("", attr, [random.randint(20, 100) for _ in range(6)],
              radius=[0, 45], center=[25, 50], rosetype='area')
    chart.add("", attr, [random.randint(0, 100) for _ in range(6)],
              radius=[50, 55], center=[65, 50], is_random=True)
    chart.add("", attr, [random.randint(20, 100) for _ in range(6)],
              radius=[0, 45], center=[65, 50], rosetype='radius')
    page.add(chart)

    chart = Pie('各类电影中"好片"所占的比例', "数据来着豆瓣",
                title_pos='center', **style.init_style)
    chart.add("", ["剧情", ""], [25, 75], center=[10, 30], radius=[18, 24],
              label_pos='center', is_label_show=True, label_text_color=None, )
    chart.add("", ["奇幻", ""], [24, 76], center=[30, 30], radius=[18, 24],
              label_pos='center', is_label_show=True, label_text_color=None,
              legend_pos='left')
    chart.add("", ["爱情", ""], [14, 86], center=[50, 30], radius=[18, 24],
              label_pos='center', is_label_show=True, label_text_color=None)
    chart.add("", ["惊悚", ""], [11, 89], center=[70, 30], radius=[18, 24],
              label_pos='center', is_label_show=True, label_text_color=None)
    chart.add("", ["冒险", ""], [27, 73], center=[90, 30], radius=[18, 24],
              label_pos='center', is_label_show=True, label_text_color=None)
    chart.add("", ["动作", ""], [15, 85], center=[10, 70], radius=[18, 24],
              label_pos='center', is_label_show=True, label_text_color=None)
    chart.add("", ["喜剧", ""], [54, 46], center=[30, 70], radius=[18, 24],
              label_pos='center', is_label_show=True, label_text_color=None)
    chart.add("", ["科幻", ""], [26, 74], center=[50, 70], radius=[18, 24],
              label_pos='center', is_label_show=True, label_text_color=None)
    chart.add("", ["悬疑", ""], [25, 75], center=[70, 70], radius=[18, 24],
              label_pos='center', is_label_show=True, label_text_color=None)
    chart.add("", ["犯罪", ""], [28, 72], center=[90, 70], radius=[18, 24],
              label_pos='center', is_label_show=True, label_text_color=None,
              is_legend_show=True, legend_top="center")
    page.add(chart)

    return page
