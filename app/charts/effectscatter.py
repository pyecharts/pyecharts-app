from pyecharts import EffectScatter, Page, Style
from app.charts.constants import WIDTH, HEIGHT


def create_charts():
    page = Page()

    style = Style(
        width=WIDTH, height=HEIGHT
    )

    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [25, 20, 15, 10, 60, 33]
    chart = EffectScatter("动态散点图-默认", **style.init_style)
    chart.add("effectScatter", v1, v2)
    page.add(chart)

    chart = EffectScatter("动态散点图-自定义", **style.init_style)
    chart.add("", [10], [10], symbol_size=20, effect_scale=3.5,
              effect_period=3, symbol="pin")
    chart.add("", [20], [20], symbol_size=12, effect_scale=4.5,
              effect_period=4, symbol="rect")
    chart.add("", [30], [30], symbol_size=30, effect_scale=5.5,
              effect_period=5, symbol="roundRect")
    chart.add("", [40], [40], symbol_size=10, effect_scale=6.5,
              effect_brushtype='fill', symbol="diamond")
    chart.add("", [50], [50], symbol_size=16, effect_scale=5.5,
              effect_period=3, symbol="arrow")
    chart.add("", [60], [60], symbol_size=6, effect_scale=2.5,
              effect_period=3, symbol="triangle")
    page.add(chart)

    return page
