# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1778317687.6536746
_enable_loop = True
_template_filename = 'res/templates/base_public.html'
_template_uri = 'base_public.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html lang="fr">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>CinéMatch</title>\n    <link rel="stylesheet" href="/static/style.css">\n</head>\n<body>\n<header>\n    <h1>CinéMatch</h1>\n    <p>Le bon film selon ton humeur</p>\n</header>\n\n<nav>\n    <a href="/">Accueil</a>\n    <a href="/moods">Humeurs</a>\n    <a href="/search">Recherche</a>\n    <a href="/admin">Admin</a>\n</nav>\n\n<main>\n    ')
        __M_writer(str(self.body()))
        __M_writer('\n</main>\n\n<footer>CinéMatch - SAE 2.03</footer>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/base_public.html", "uri": "base_public.html", "source_encoding": "utf-8", "line_map": {"16": 0, "22": 1, "23": 23, "24": 23, "30": 24}}
__M_END_METADATA
"""
