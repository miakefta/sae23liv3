# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1778317687.6133666
_enable_loop = True
_template_filename = 'res/templates/public_index.html'
_template_uri = 'public_index.html'
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
        humeurs = context.get('humeurs', []); films = context.get('films', []) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['films','humeurs'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<section class="hero">\n    <h2>Bienvenue sur CinéMatch</h2>\n    <p>Choisis une humeur et trouve rapidement un film adapté à ton envie du moment.</p>\n    <div class="actions">\n        <a class="button" href="/moods">Choisir une humeur</a>\n        <a class="button button-light" href="/search">Rechercher</a>\n    </div>\n</section>\n\n<h3 class="section-title">Humeurs disponibles</h3>\n<div class="grid">\n')
        for humeur in humeurs:
            __M_writer('    <div class="card">\n        <h3>')
            __M_writer(str(humeur.nom))
            __M_writer('</h3>\n        <p>')
            __M_writer(str(humeur.description))
            __M_writer('</p>\n        <a class="button button-light" href="/mood?humeur_id=')
            __M_writer(str(humeur.id_humeur))
            __M_writer('">Voir les films</a>\n    </div>\n')
        __M_writer('</div>\n\n<h3 class="section-title">Quelques films</h3>\n<div class="grid">\n')
        for film in films[:5]:
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
{"filename": "res/templates/public_index.html", "uri": "public_index.html", "source_encoding": "utf-8", "line_map": {"27": 0, "32": 1, "33": 2, "34": 3, "37": 2, "38": 15, "39": 16, "40": 17, "41": 17, "42": 18, "43": 18, "44": 19, "45": 19, "46": 22, "47": 26, "48": 27, "49": 28, "50": 28, "51": 29, "52": 29, "53": 29, "54": 29, "55": 30, "56": 30, "57": 31, "58": 31, "59": 32, "60": 32, "61": 35, "67": 61}}
__M_END_METADATA
"""
