import os
import json

from pyecharts import Sankey, Page


def sankey_charts():
    page = Page()

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
    chart1 = Sankey("桑基图示例", width=1200, height=600)
    chart1.add("sankey", nodes, links, line_opacity=0.2,
               line_curve=0.5, line_color='source', is_label_show=True,
               label_pos='right')
    page.add(chart1)

    with open(os.path.join(".", "data", "energy.json"), "r", encoding="utf-8") as f:
        j = json.load(f)
    chart2 = Sankey("桑基图示例", width=1200, height=600)
    chart2.add("sankey", nodes=j['nodes'], links=j['links'], line_opacity=0.2,
               line_curve=0.5, line_color='source',
               is_label_show=True, label_pos='right')
    page.add(chart2)

    return page

sankey_charts()