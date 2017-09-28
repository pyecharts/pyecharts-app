from pyecharts import Liquid, Page


def liquid_charts():
    page = Page()

    chart = Liquid("水球图-单数据")
    chart.add("Liquid", [0.6])
    page.add(chart)

    chart = Liquid("水球图-多数据")
    chart.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
    page.add(chart)

    chart = Liquid("水球图-动画静止")
    chart.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_animation=False,
              shape='diamond')
    page.add(chart)

    return page
