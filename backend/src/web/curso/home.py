# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from curso.modelo import Curso
from tekton import router
from web.curso.crud import salvar, detalhar


def index(_write_tmpl, _usuario_corrente):
    salvar_path = router.to_path(salvar)
    query = Curso.query_encontrar_cursos_de_usuario(_usuario_corrente.key)
    cursos = query.fetch()
    for c in cursos:
        c.detalhar_path = router.to_path(detalhar, c.key.id())
    _write_tmpl('curso_home.html', {'cursos': cursos, 'salvar_path': salvar_path})