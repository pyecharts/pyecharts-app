from pyecharts import Liquid, Page


def liquid_charts():
    page = Page()

    chart1 = Liquid("水球图-单数据")
    chart1.add("Liquid", [0.6])
    page.add(chart1)

    chart2 = Liquid("水球图-多数据")
    chart2.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
    page.add(chart2)

    chart3 = Liquid("水球图-动画静止")
    chart3.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_animation=False,
               shape='diamond')
    page.add(chart3)

    return page
