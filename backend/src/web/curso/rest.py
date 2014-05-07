# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from curso.modelo import Curso


def listar_cursos(_resp, _usuario_corrente):
    query = Curso.query_encontrar_cursos_de_usuario(_usuario_corrente.key)
    cursos = query.fetch()
    cursos_dct = [{'id': c.key.id(), 'nome': c.nome} for c in cursos]
    json_str = json.dumps(cursos_dct)
    _resp.write(json_str)


def salvar_curso(_resp, _usuario_corrente, nome, descricao):
    curso = Curso(dono_key=_usuario_corrente.key,
                  nome=nome,
                  descricao=descricao)
    key = curso.put()
    json_str = json.dumps({'id': key.id()})
    _resp.write(json_str)

