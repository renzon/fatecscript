# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import email
from google.appengine.api import users
from usuario.modelo import Usuario


def execute(next_process, handler, dependencies, **kwargs):
    google_user = users.get_current_user()
    if google_user:
        google_id = google_user.user_id()
        query = Usuario.query_encontrar_por_google_id(google_id)
        meu_usuario = query.get()
        if meu_usuario is None:
            meu_usuario = Usuario(google_id=google_id,
                                  nome=google_user.nickname(),
                                  email=google_user.email())
            meu_usuario.put()
        dependencies['_usuario_corrente'] = meu_usuario
        dependencies['_logout_url'] = users.create_logout_url('/')
    else:
        req = handler.request
        dependencies['_login_url'] = users.create_login_url(req.uri)

    next_process(dependencies, **kwargs)
