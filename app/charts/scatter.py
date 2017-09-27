import os

from pyecharts import Scatter, Page


def scatter_charts():
    page = Page()

    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [10, 20, 30, 40, 50, 60]
    chart1 = Scatter("散点图示例")
    chart1.add("A", v1, v2)
    chart1.add("B", v1[::-1], v2)
    page.add(chart1)

    chart2 = Scatter("散点图示例")
    chart2.add("A", ["a", "b", "c", "d", "e", "f"], v2)
    chart2.add("B", ["a", "b", "c", "d", "e", "f"], v1[::-1],
               xaxis_type="category")
    page.add(chart2)

    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [10, 20, 30, 40, 50, 60]
    chart3 = Scatter("散点图示例")
    chart3.add("A", v1, v2)
    chart3.add("B", v1[::-1], v2, is_visualmap=True)
    page.add(chart3)

    chart4 = Scatter("散点图示例")
    chart4.add("A", v1, v2)
    chart4.add("B", v1[::-1], v2, is_visualmap=True, visual_type='size',
                visual_range_size=[20, 80])
    page.add(chart4)

    chart5 = Scatter("散点图示例")
    v1, v2 = chart5.draw(os.path.join(".", "data", "pyecharts.png"))
    chart5.add("pyecharts", v1, v2, is_random=True)
    page.add(chart5)

    chart6 = Scatter("散点图示例", width=800, height=480)
    v1, v2 = chart6.draw(os.path.join(".", "data", "love.png"))
    chart6.add("Love", v1, v2)
    page.add(chart6)

    chart7 = Scatter("散点图示例", width=1000, height=480)
    v1, v2 = chart7.draw(os.path.join(".", "data", "cup.png"))
    chart7.add("Cup", v1, v2)
    page.add(chart7)

    chart8 = Scatter("散点图示例", width=1000, height=480)
    v1, v2 = chart8.draw(os.path.join(".", "data", "cup.png"))
    chart8.add("Cup", v1, v2, label_color=["#000"])
    page.add(chart8)

    data = [
        [28604, 77, 17096869],
        [31163, 77.4, 27662440],
        [1516, 68, 1154605773],
        [13670, 74.7, 10582082],
        [28599, 75, 4986705],
        [29476, 77.1, 56943299],
        [31476, 75.4, 78958237],
        [28666, 78.1, 254830],
        [1777, 57.7, 870601776],
        [29550, 79.1, 122249285],
        [2076, 67.9, 20194354],
        [12087, 72, 42972254],
        [24021, 75.4, 3397534],
        [43296, 76.8, 4240375],
        [10088, 70.8, 38195258],
        [19349, 69.6, 147568552],
        [10670, 67.3, 53994605],
        [26424, 75.7, 57110117],
        [37062, 75.4, 252847810]
    ]

    x_lst = [v[0] for v in data]
    y_lst = [v[1] for v in data]
    extra_data = [v[2] for v in data]
    chart9 = Scatter()
    chart9.add("scatter", x_lst, y_lst, extra_data=extra_data, is_visualmap=True,
           visual_dimension=2, visual_orient='horizontal',
           visual_type='size', visual_range=[254830, 1154605773],
           visual_text_color='#000')
    page.add(chart9)

    return page
