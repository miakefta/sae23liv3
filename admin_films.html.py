# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1778317713.6325307
_enable_loop = True
_template_filename = 'res/templates/admin_films.html'
_template_uri = 'admin_films.html'
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
        films = context.get('films', []) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['films'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<section class="panel center">\n    <h2>Gestion des films</h2>\n    <p class="muted">Liste des films enregistrés dans la base.</p>\n    <a class="button" href="/add_film_form">Ajouter un film</a>\n</section>\n\n<div class="table-box">\n<table>\n    <tr>\n        <th>ID</th>\n        <th>Titre</th>\n        <th>Année</th>\n        <th>Genre</th>\n        <th>Humeur</th>\n        <th>Note</th>\n        <th>Actions</th>\n    </tr>\n')
        for film in films:
            __M_writer('    <tr>\n        <td>')
            __M_writer(str(film["id_film"]))
            __M_writer('</td>\n        <td><strong>')
            __M_writer(str(film["titre"]))
            __M_writer('</strong></td>\n        <td>')
            __M_writer(str(film["annee"]))
            __M_writer('</td>\n        <td>')
            __M_writer(str(film["genre_nom"]))
            __M_writer('</td>\n        <td><span class="badge">')
            __M_writer(str(film["humeur_nom"]))
            __M_writer('</span></td>\n        <td>')
            __M_writer(str(film["note"]))
            __M_writer('/10</td>\n        <td>\n            <a href="/film_detail?film_id=')
            __M_writer(str(film['id_film']))
            __M_writer('">Voir</a>\n            <span class="sep">|</span>\n            <a class="danger" href="/delete_film?film_id=')
            __M_writer(str(film['id_film']))
            __M_writer('">Supprimer</a>\n        </td>\n    </tr>\n')
        __M_writer('</table>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/admin_films.html", "uri": "admin_films.html", "source_encoding": "utf-8", "line_map": {"27": 0, "32": 1, "33": 2, "34": 3, "37": 2, "38": 21, "39": 22, "40": 23, "41": 23, "42": 24, "43": 24, "44": 25, "45": 25, "46": 26, "47": 26, "48": 27, "49": 27, "50": 28, "51": 28, "52": 30, "53": 30, "54": 32, "55": 32, "56": 36, "62": 56}}
__M_END_METADATA
"""
