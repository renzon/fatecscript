# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import tmpl


def execute(next_process, handler, dependencies, **kwargs):
    def write_tmpl(template_name, values=None):
        path = handler.request.path
        dct = {'_path': path,
               '_usuario_corrente':dependencies.get('_usuario_corrente'),
               '_logout_url':dependencies.get('_logout_url'),
               '_login_url':dependencies.get('_login_url')
               }
        dct.update(values or {})
        return handler.response.write(tmpl.render(template_name, dct))
    dependencies["_write_tmpl"] = write_tmpl
    dependencies["_render"] = tmpl.render
    next_process(dependencies, **kwargs)
