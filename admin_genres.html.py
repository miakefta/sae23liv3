# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1778317715.2327213
_enable_loop = True
_template_filename = 'res/templates/admin_genres.html'
_template_uri = 'admin_genres.html'
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
        genres = context.get('genres', []) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['genres'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<section class="panel center">\n    <h2>Gestion des genres</h2>\n    <p class="muted">Liste simple des genres disponibles.</p>\n    <a class="button" href="/add_genre_form">Ajouter un genre</a>\n</section>\n\n<div class="grid">\n')
        for genre in genres:
            __M_writer('    <div class="card">\n        <h3>')
            __M_writer(str(genre.nom))
            __M_writer('</h3>\n        <a class="button button-danger" href="/delete_genre?genre_id=')
            __M_writer(str(genre.id_genre))
            __M_writer('">Supprimer</a>\n    </div>\n')
        __M_writer('</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/admin_genres.html", "uri": "admin_genres.html", "source_encoding": "utf-8", "line_map": {"27": 0, "32": 1, "33": 2, "34": 3, "37": 2, "38": 11, "39": 12, "40": 13, "41": 13, "42": 14, "43": 14, "44": 17, "50": 44}}
__M_END_METADATA
"""
