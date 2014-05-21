# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from base import GAETestCase
from curso.modelo import Curso
from mock import Mock
from usuario.modelo import Usuario
from web.curso import rest


class ListarCursosTests(GAETestCase):
    def test_sucesso(self):
        usuario_logado = Usuario()
        usuario_logado.put()
        curso = Curso(nome='PyPratico',
                      dono_key=usuario_logado.key)
        curso.put()
        resposta_mock = Mock()
        rest.listar_cursos(resposta_mock, usuario_logado)
        lista_dct = [{'id': curso.key.id(), 'nome': curso.nome}]
        json_str = json.dumps(lista_dct)
        resposta_mock.write.assert_called_once_with(json_str)

