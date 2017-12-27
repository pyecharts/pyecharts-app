from flask import render_template
import app.charts as charts

from . import app


@app.route("/")
def hello():
    return render_template('index.html',
                           title='首页')


@app.route('/bar')
def bar():
    _bar = charts.bar.create_charts()
    return render_template('base.html',
                           title='柱状图',
                           source_file='bar',
                           myechart=_bar.render_embed(),
                           script_list=_bar.get_js_dependencies())


@app.route('/bar3d')
def bar3d():
    _bar3d = charts.bar3d.create_charts()
    return render_template('base.html',
                           title='3D柱状图',
                           source_file='bar3d',
                           myechart=_bar3d.render_embed(),
                           script_list=_bar3d.get_js_dependencies())


@app.route('/boxplot')
def boxplot():
    _boxplot = charts.boxplot.create_charts()
    return render_template('base.html',
                           title='箱线图',
                           source_file='boxplot',
                           myechart=_boxplot.render_embed(),
                           script_list=_boxplot.get_js_dependencies())


@app.route('/effectscatter')
def effectscatter():
    _es = charts.effectscatter.create_charts()
    return render_template('base.html',
                           title='动态散点图',
                           source_file='effectscatter',
                           myechart=_es.render_embed(),
                           script_list=_es.get_js_dependencies())


@app.route('/funnel')
def funnel():
    _funnel = charts.funnel.create_charts()
    return render_template('base.html',
                           title='漏斗图',
                           source_file='funnel',
                           myechart=_funnel.render_embed(),
                           script_list=_funnel.get_js_dependencies())


@app.route('/gauge')
def gauge():
    _gauge = charts.gauge.create_charts()
    return render_template('base.html',
                           title='仪表盘',
                           source_file='gauge',
                           myechart=_gauge.render_embed(),
                           script_list=_gauge.get_js_dependencies())


@app.route('/geo')
def geo():
    _geo = charts.geo.create_charts()
    return render_template('base.html',
                           title='地理坐标系',
                           source_file='geo',
                           myechart=_geo.render_embed(),
                           script_list=_geo.get_js_dependencies())


@app.route('/geolines')
def geolines():
    _geolines = charts.geolines.create_charts()
    return render_template('base.html',
                           title='地理坐标系线图',
                           source_file='geolines',
                           myechart=_geolines.render_embed(),
                           script_list=_geolines.get_js_dependencies())


@app.route('/graph')
def graph():
    _graph = charts.graph.create_charts()
    return render_template('base.html',
                           title='关系图',
                           source_file='graph',
                           myechart=_graph.render_embed(),
                           script_list=_graph.get_js_dependencies())


@app.route('/heatmap')
def heatmap():
    _heatmap = charts.heatmap.create_charts()
    return render_template('base.html',
                           title='热力图',
                           source_file='heatmap',
                           myechart=_heatmap.render_embed(),
                           script_list=_heatmap.get_js_dependencies())


@app.route('/kline')
def kline():
    _kline = charts.kline.create_charts()
    return render_template('base.html',
                           title='K线图',
                           source_file='kline',
                           myechart=_kline.render_embed(),
                           script_list=_kline.get_js_dependencies())


@app.route('/line')
def line():
    _line = charts.line.create_charts()
    return render_template('base.html',
                           title='折线图',
                           source_file='line',
                           myechart=_line.render_embed(),
                           script_list=_line.get_js_dependencies())


@app.route('/line3d')
def line3d():
    _line3d = charts.line3d.create_charts()
    return render_template('base.html',
                           title='3D折线图',
                           source_file='line3d',
                           myechart=_line3d.render_embed(),
                           script_list=_line3d.get_js_dependencies())


@app.route('/liquid')
def liquid():
    _liquid = charts.liquid.create_charts()
    return render_template('base.html',
                           title='水球图',
                           source_file='liquid',
                           myechart=_liquid.render_embed(),
                           script_list=_liquid.get_js_dependencies())


@app.route('/map')
def map():
    _map = charts.map.create_charts()
    return render_template('base.html',
                           title='地图',
                           source_file='map',
                           myechart=_map.render_embed(),
                           script_list=_map.get_js_dependencies())


@app.route('/parallel')
def parallel():
    _parallel = charts.parallel.create_charts()
    return render_template('base.html',
                           title='平行坐标系',
                           source_file='parallel',
                           myechart=_parallel.render_embed(),
                           script_list=_parallel.get_js_dependencies())


@app.route('/pie')
def pie():
    _pie = charts.pie.create_charts()
    return render_template('base.html',
                           title='饼图',
                           source_file='pie',
                           myechart=_pie.render_embed(),
                           script_list=_pie.get_js_dependencies())


@app.route('/polar')
def polar():
    _polar = charts.polar.create_charts()
    return render_template('base.html',
                           title='极坐标系',
                           source_file='polar',
                           myechart=_polar.render_embed(),
                           script_list=_polar.get_js_dependencies())


@app.route('/radar')
def radar():
    _radar = charts.radar.create_charts()
    return render_template('base.html',
                           title='雷达图',
                           source_file='radar',
                           myechart=_radar.render_embed(),
                           script_list=_radar.get_js_dependencies())


@app.route('/sankey')
def sankey():
    _sankey = charts.sankey.create_charts()
    return render_template('base.html',
                           title='桑基图',
                           source_file='sankey',
                           myechart=_sankey.render_embed(),
                           script_list=_sankey.get_js_dependencies())


@app.route('/scatter')
def scatter():
    _scatter = charts.scatter.create_charts()
    return render_template('base.html',
                           title='散点图',
                           source_file='scatter',
                           myechart=_scatter.render_embed(),
                           script_list=_scatter.get_js_dependencies())


@app.route('/scatter3d')
def scatter3d():
    _scatter3d = charts.scatter3d.create_charts()
    return render_template('base.html',
                           title='3D散点图',
                           source_file='scatter3d',
                           myechart=_scatter3d.render_embed(),
                           script_list=_scatter3d.get_js_dependencies())


@app.route('/themeriver')
def themeriver():
    _themeriver = charts.themeriver.create_charts()
    return render_template('base.html',
                           title='主题河流图',
                           source_file='themeriver',
                           myechart=_themeriver.render_embed(),
                           script_list=_themeriver.get_js_dependencies())


@app.route('/treemap')
def treemap():
    _treemap = charts.treemap.create_charts()
    return render_template('base.html',
                           title='树图',
                           myechart=_treemap.render_embed(),
                           script_list=_treemap.get_js_dependencies())


@app.route('/wordcloud')
def wordcloud():
    _wordcloud = charts.wordcloud.create_charts()
    return render_template('base.html',
                           title='词云图',
                           source_file='wordcloud',
                           myechart=_wordcloud.render_embed(),
                           script_list=_wordcloud.get_js_dependencies())


@app.route('/grid')
def grid():
    _grid = charts.grid.create_charts()
    return render_template('base.html',
                           title='Grid类',
                           source_file='grid',
                           myechart=_grid.render_embed(),
                           script_list=_grid.get_js_dependencies())


@app.route('/overlap')
def overlap():
    _overlap = charts.overlap.create_charts()
    return render_template('base.html',
                           title='Overlap类',
                           source_file='overlap',
                           myechart=_overlap.render_embed(),
                           script_list=_overlap.get_js_dependencies())


@app.route('/timeline')
def timeline():
    _timeline = charts.timeline.create_charts()
    return render_template('base.html',
                           title='Timeline类',
                           source_file='timeline',
                           myechart=_timeline.render_embed(),
                           script_list=_timeline.get_js_dependencies())


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
