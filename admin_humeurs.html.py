# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1778317714.4607272
_enable_loop = True
_template_filename = 'res/templates/admin_humeurs.html'
_template_uri = 'admin_humeurs.html'
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
        humeurs = context.get('humeurs', []) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['humeurs'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<section class="panel center">\n    <h2>Gestion des humeurs</h2>\n    <p class="muted">Les humeurs permettent de conseiller les films autrement.</p>\n    <a class="button" href="/add_humeur_form">Ajouter une humeur</a>\n</section>\n\n<div class="grid">\n')
        for humeur in humeurs:
            __M_writer('    <div class="card">\n        <h3>')
            __M_writer(str(humeur.nom))
            __M_writer('</h3>\n        <p>')
            __M_writer(str(humeur.description))
            __M_writer('</p>\n        <a class="button button-danger" href="/delete_humeur?humeur_id=')
            __M_writer(str(humeur.id_humeur))
            __M_writer('">Supprimer</a>\n    </div>\n')
        __M_writer('</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/admin_humeurs.html", "uri": "admin_humeurs.html", "source_encoding": "utf-8", "line_map": {"27": 0, "32": 1, "33": 2, "34": 3, "37": 2, "38": 11, "39": 12, "40": 13, "41": 13, "42": 14, "43": 14, "44": 15, "45": 15, "46": 18, "52": 46}}
__M_END_METADATA
"""
