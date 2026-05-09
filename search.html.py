# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1778317715.8298485
_enable_loop = True
_template_filename = 'res/templates/search.html'
_template_uri = 'search.html'
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
    return runtime._inherit_from(context, 'base_public.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        films = context.get('films', []); titre = context.get('titre', ''); genre = context.get('genre', ''); annee = context.get('annee', '') 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['films','annee','genre','titre'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<section class="panel center">\n    <h2>Recherche de films</h2>\n    <p class="muted">Recherche par titre, genre ou année.</p>\n</section>\n\n<section class="panel">\n    <form class="form-grid" method="get" action="/search">\n        <div>\n            <label>Titre</label>\n            <input type="text" name="titre" value="')
        __M_writer(str(titre))
        __M_writer('" placeholder="Ex : Inception">\n        </div>\n        <div>\n            <label>Genre</label>\n            <input type="text" name="genre" value="')
        __M_writer(str(genre))
        __M_writer('" placeholder="Ex : Action">\n        </div>\n        <div>\n            <label>Année</label>\n            <input type="number" name="annee" value="')
        __M_writer(str(annee))
        __M_writer('" placeholder="Ex : 2010">\n        </div>\n        <button type="submit">Rechercher</button>\n    </form>\n</section>\n\n<div class="grid">\n')
        for film in films:
            __M_writer('    <div class="card">\n        <h3>')
            __M_writer(str(film["titre"]))
            __M_writer('</h3>\n        <p>')
            __M_writer(str(film["annee"]))
            __M_writer(' • ')
            __M_writer(str(film["genre_nom"]))
            __M_writer('</p>\n        <p><span class="badge">')
            __M_writer(str(film["humeur_nom"]))
            __M_writer('</span></p>\n        <p>Note : ')
            __M_writer(str(film["note"]))
            __M_writer('/10</p>\n        <a class="button button-light" href="/film_detail?film_id=')
            __M_writer(str(film['id_film']))
            __M_writer('">Détail</a>\n    </div>\n')
        __M_writer('</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/search.html", "uri": "search.html", "source_encoding": "utf-8", "line_map": {"27": 0, "32": 1, "33": 2, "34": 3, "37": 2, "38": 13, "39": 13, "40": 17, "41": 17, "42": 21, "43": 21, "44": 28, "45": 29, "46": 30, "47": 30, "48": 31, "49": 31, "50": 31, "51": 31, "52": 32, "53": 32, "54": 33, "55": 33, "56": 34, "57": 34, "58": 37, "64": 58}}
__M_END_METADATA
"""
