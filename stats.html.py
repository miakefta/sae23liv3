# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1778317836.56655
_enable_loop = True
_template_filename = 'res/templates/stats.html'
_template_uri = 'stats.html'
_source_encoding = 'utf-8'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base_admin.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        stats_humeur = context.get('stats_humeur', context.get('stats_by_humeur', [])); stats_genre = context.get('stats_genre', context.get('stats_by_genre', [])); stats_annee = context.get('stats_annee', context.get('stats_by_annee', [])) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['stats_genre','stats_annee','stats_humeur'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<section class="panel center">\n    <h2>Statistiques</h2>\n    <p class="muted">Vue simple des données de l\'application.</p>\n</section>\n\n<div class="grid">\n    <div class="card">\n        <h3>Films par humeur</h3>\n')
        for row in stats_humeur:
            __M_writer('        <p>')
            __M_writer(str(row.get('humeur', '')))
            __M_writer(' : <strong>')
            __M_writer(str(row.get('total', 0)))
            __M_writer('</strong></p>\n')
        __M_writer('    </div>\n    <div class="card">\n        <h3>Films par genre</h3>\n')
        for row in stats_genre:
            __M_writer('        <p>')
            __M_writer(str(row.get('genre', '')))
            __M_writer(' : <strong>')
            __M_writer(str(row.get('total', 0)))
            __M_writer('</strong></p>\n')
        __M_writer('    </div>\n    <div class="card">\n        <h3>Films par année</h3>\n')
        for row in stats_annee:
            __M_writer('        <p>')
            __M_writer(str(row.get('annee', '')))
            __M_writer(' : <strong>')
            __M_writer(str(row.get('total', 0)))
            __M_writer('</strong></p>\n')
        __M_writer('    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/stats.html", "uri": "stats.html", "source_encoding": "utf-8", "line_map": {"27": 0, "32": 1, "33": 2, "34": 3, "37": 2, "38": 12, "39": 13, "40": 13, "41": 13, "42": 13, "43": 13, "44": 15, "45": 18, "46": 19, "47": 19, "48": 19, "49": 19, "50": 19, "51": 21, "52": 24, "53": 25, "54": 25, "55": 25, "56": 25, "57": 25, "58": 27, "64": 58}}
__M_END_METADATA
"""
