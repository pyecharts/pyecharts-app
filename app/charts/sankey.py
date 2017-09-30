from pyecharts import Sankey, Page
from .constants import HEIGHT, WIDTH, ENERGY


def sankey_charts():
    page = Page()

    chart_init = {
        "width": WIDTH,
        "height": HEIGHT,
    }

    nodes = [
        {'name': 'category1'}, {'name': 'category2'}, {'name': 'category3'},
        {'name': 'category4'}, {'name': 'category5'}, {'name': 'category6'},
    ]

    links = [
        {'source': 'category1', 'target': 'category2', 'value': 10},
        {'source': 'category2', 'target': 'category3', 'value': 15},
        {'source': 'category3', 'target': 'category4', 'value': 20},
        {'source': 'category5', 'target': 'category6', 'value': 25}
    ]
    chart = Sankey("桑基图-默认", **chart_init)
    chart.add("sankey", nodes, links, line_opacity=0.2,
              line_curve=0.5, line_color='source', is_label_show=True,
              label_pos='right')
    page.add(chart)

    chart = Sankey("桑基图-自定义", **chart_init)
    chart.add("sankey", nodes=ENERGY['nodes'], links=ENERGY['links'],
              line_opacity=0.2, line_curve=0.5, line_color='source',
              is_label_show=True, label_pos='right')
    page.add(chart)

    return page
