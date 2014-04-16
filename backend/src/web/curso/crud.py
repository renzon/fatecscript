# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from curso.modelo import Curso
from tekton import router


def salvar(_handler,_usuario_corrente, nome, descricao):
    from web.curso.home import index

    curso = Curso(nome=nome, descricao=descricao,
                  dono_key=_usuario_corrente.key)
    curso.put()
    path = router.to_path(index)
    _handler.redirect(path)


def detalhar(_write_tmpl, curso_id):
    curso = Curso.get_by_id(int(curso_id))
    _write_tmpl('curso_detalhe.html', {'curso': curso})