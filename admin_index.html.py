# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1778317710.745464
_enable_loop = True
_template_filename = 'res/templates/admin_index.html'
_template_uri = 'admin_index.html'
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
        __M_writer('\n\n<section class="hero">\n    <h2>Dashboard admin</h2>\n    <p>Choisis une rubrique pour gérer le contenu de ton application.</p>\n</section>\n\n<div class="grid">\n    <a class="card link-card" href="/admin_films"><h3>Films</h3><p>Voir, ajouter ou supprimer des films.</p></a>\n    <a class="card link-card" href="/admin_humeurs"><h3>Humeurs</h3><p>Gérer les humeurs proposées.</p></a>\n    <a class="card link-card" href="/admin_genres"><h3>Genres</h3><p>Gérer les genres de films.</p></a>\n    <a class="card link-card" href="/search"><h3>Recherche</h3><p>Retrouver rapidement un film.</p></a>\n    <a class="card link-card" href="/stats"><h3>Statistiques</h3><p>Voir les données principales.</p></a>\n    <a class="card link-card" href="/"><h3>Site public</h3><p>Retour à l\'accueil utilisateur.</p></a>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/admin_index.html", "uri": "admin_index.html", "source_encoding": "utf-8", "line_map": {"27": 0, "32": 1, "38": 32}}
__M_END_METADATA
"""
