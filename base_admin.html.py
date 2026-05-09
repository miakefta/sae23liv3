# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1778317710.783484
_enable_loop = True
_template_filename = 'res/templates/base_admin.html'
_template_uri = 'base_admin.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html lang="fr">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Admin - CinéMatch</title>\n    <link rel="stylesheet" href="/static/style.css">\n</head>\n<body>\n<header>\n    <h1>Administration CinéMatch</h1>\n    <p>Gestion des films, genres et humeurs</p>\n</header>\n\n<nav>\n    <a href="/">Accueil public</a>\n    <a href="/admin">Dashboard</a>\n    <a href="/admin_films">Films</a>\n    <a href="/admin_humeurs">Humeurs</a>\n    <a href="/admin_genres">Genres</a>\n    <a href="/search">Recherche</a>\n    <a href="/stats">Stats</a>\n</nav>\n\n<main>\n    ')
        __M_writer(str(self.body()))
        __M_writer('\n</main>\n\n<footer>Backoffice CinéMatch</footer>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/base_admin.html", "uri": "base_admin.html", "source_encoding": "utf-8", "line_map": {"16": 0, "22": 1, "23": 26, "24": 26, "30": 24}}
__M_END_METADATA
"""
