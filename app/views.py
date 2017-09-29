from flask import render_template
from app.charts import *

from . import app


@app.route("/")
def hello():
    return render_template('index.html',
                           title='首页')


@app.route('/bar')
def bar():
    _bar = bar_charts()
    return render_template('base.html',
                           title='柱状图',
                           myechart=_bar.render_embed(),
                           script_list=_bar.get_js_dependencies())


@app.route('/bar3d')
def bar3d():
    _bar3d = bar3d_charts()
    return render_template('base.html',
                           title='3D柱状图',
                           myechart=_bar3d.render_embed(),
                           script_list=_bar3d.get_js_dependencies())


@app.route('/boxplot')
def boxplot():
    _boxplot = boxplot_charts()
    return render_template('base.html',
                           title='箱线图',
                           myechart=_boxplot.render_embed(),
                           script_list=_boxplot.get_js_dependencies())


@app.route('/effectscatter')
def effectscatter():
    _es = effectscatter_charts()
    return render_template('base.html',
                           title='动态散点图',
                           myechart=_es.render_embed(),
                           script_list=_es.get_js_dependencies())


@app.route('/funnel')
def funnel():
    _funnel = funnel_charts()
    return render_template('base.html',
                           title='仪表盘',
                           myechart=_funnel.render_embed(),
                           script_list=_funnel.get_js_dependencies())


@app.route('/gauge')
def gauge():
    _gauge = gauge_charts()
    return render_template('base.html',
                           title='漏斗图',
                           myechart=_gauge.render_embed(),
                           script_list=_gauge.get_js_dependencies())


@app.route('/geo')
def geo():
    _geo = geo_charts()
    return render_template('base.html',
                           title='地理坐标系',
                           myechart=_geo.render_embed(),
                           script_list=_geo.get_js_dependencies())


@app.route('/graph')
def graph():
    _graph = graph_charts()
    return render_template('base.html',
                           title='关系图',
                           myechart=_graph.render_embed(),
                           script_list=_graph.get_js_dependencies())


@app.route('/heatmap')
def heatmap():
    _heatmap = heatmap_charts()
    return render_template('base.html',
                           title='热力图',
                           myechart=_heatmap.render_embed(),
                           script_list=_heatmap.get_js_dependencies())


@app.route('/kline')
def kline():
    _kline = kline_charts()
    return render_template('base.html',
                           title='K线图',
                           myechart=_kline.render_embed(),
                           script_list=_kline.get_js_dependencies())


@app.route('/line')
def line():
    _line = line_charts()
    return render_template('base.html',
                           title='折线图',
                           myechart=_line.render_embed(),
                           script_list=_line.get_js_dependencies())


@app.route('/line3d')
def line3d():
    _line3d = line3d_charts()
    return render_template('base.html',
                           title='3D折线图',
                           myechart=_line3d.render_embed(),
                           script_list=_line3d.get_js_dependencies())


@app.route('/liquid')
def liquid():
    _liquid = liquid_charts()
    return render_template('base.html',
                           title='水球图',
                           myechart=_liquid.render_embed(),
                           script_list=_liquid.get_js_dependencies())


@app.route('/map')
def map():
    _map = map_charts()
    return render_template('base.html',
                           title='地图',
                           myechart=_map.render_embed(),
                           script_list=_map.get_js_dependencies())


@app.route('/parallel')
def parallel():
    _parallel = parallel_charts()
    return render_template('base.html',
                           title='平行坐标系',
                           myechart=_parallel.render_embed(),
                           script_list=_parallel.get_js_dependencies())


@app.route('/pie')
def pie():
    _pie = pie_charts()
    return render_template('base.html',
                           title='饼图',
                           myechart=_pie.render_embed(),
                           script_list=_pie.get_js_dependencies())


@app.route('/polar')
def polar():
    _polar = polar_charts()
    return render_template('base.html',
                           title='极坐标系',
                           myechart=_polar.render_embed(),
                           script_list=_polar.get_js_dependencies())


@app.route('/radar')
def radar():
    _radar = radar_charts()
    return render_template('base.html',
                           title='雷达图',
                           myechart=_radar.render_embed(),
                           script_list=_radar.get_js_dependencies())


@app.route('/sankey')
def sankey():
    _sankey = sankey_charts()
    return render_template('base.html',
                           title='桑基图',
                           myechart=_sankey.render_embed(),
                           script_list=_sankey.get_js_dependencies())


@app.route('/scatter')
def scatter():
    _scatter = scatter_charts()
    return render_template('base.html',
                           title='散点图',
                           myechart=_scatter.render_embed(),
                           script_list=_scatter.get_js_dependencies())


@app.route('/scatter3d')
def scatter3d():
    _scatter3d = scatter3d_charts()
    return render_template('base.html',
                           title='3D散点图',
                           myechart=_scatter3d.render_embed(),
                           script_list=_scatter3d.get_js_dependencies())


@app.route('/themeriver')
def themeriver():
    _themeriver = themeriver_charts()
    return render_template('base.html',
                           title='主题河流图',
                           myechart=_themeriver.render_embed(),
                           script_list=_themeriver.get_js_dependencies())


@app.route('/wordcloud')
def wordcloud():
    _wordcloud = wordcloud_charts()
    return render_template('base.html',
                           title='词云图',
                           myechart=_wordcloud.render_embed(),
                           script_list=_wordcloud.get_js_dependencies())


@app.route('/grid')
def grid():
    _grid = grid_charts()
    return render_template('base.html',
                           title='Grid类',
                           myechart=_grid.render_embed(),
                           script_list=_grid.get_js_dependencies())


@app.route('/overlap')
def overlap():
    _overlap = overlap_charts()
    return render_template('base.html',
                           title='Overlap类',
                           myechart=_overlap.render_embed(),
                           script_list=_overlap.get_js_dependencies())


@app.route('/timeline')
def timeline():
    _timeline = timeline_charts()
    return render_template('base.html',
                           title='Timeline类',
                           myechart=_timeline.render_embed(),
                           script_list=_timeline.get_js_dependencies())


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
