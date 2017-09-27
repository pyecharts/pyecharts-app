from pyecharts import WordCloud, Page
from .constants import WIDTH, HEIGHT


def wordcloud_charts():
    page = Page()

    name = [
        'Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World',
        'Charter Communications', 'Chick Fil A', 'Planet Fitness',
        'Pitch Perfect', 'Express', 'Home', 'Johnny Depp', 'Lena Dunham',
        'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
        'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break'
    ]
    value = [
        10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112,
        965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265
    ]
    chart1 = WordCloud("词云图-默认形状", width=WIDTH, height=HEIGHT)
    chart1.add("", name, value, word_size_range=[30, 100], rotate_step=66)
    page.add(chart1)

    chart2 = WordCloud("词云图-自定义形状", width=WIDTH, height=HEIGHT)
    chart2.add("", name, value, word_size_range=[30, 100], shape='diamond')
    page.add(chart2)

    return page
