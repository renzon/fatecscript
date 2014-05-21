# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from curso.modelo import Curso
from mock import Mock
import tmpl
from usuario.modelo import Usuario
from web.curso import rest, crud


class SalvarTests(GAETestCase):
    def test_sucesso(self):
        usuario_logado = Usuario()
        usuario_logado.put()
        handler = Mock()

        crud.salvar(handler, usuario_logado, 'PyPratico', 'descricao')
        cursos = Curso.query().fetch()
        self.assertEqual(1, len(cursos))
        curso = cursos[0]
        self.assertEqual('PyPratico', curso.nome)
        self.assertEqual('descricao', curso.descricao)
        handler.redirect.assert_called_once_with('/curso')

    def test_mock(self):
        obj = Mock()
        obj.atributo.calcular('soma', 1, 2)
        obj.atributo.calcular.assert_called_once_with('soma', 1, 2)


class DetalharTests(GAETestCase):
    def test_sucesso(self):
        write_mock = Mock()
        curso = Curso(nome='Foo')
        chave = curso.put()
        crud.detalhar(write_mock, str(chave.id()))
        write_mock.assert_called_once_with('curso_detalhe.html', {'curso': curso})
        tmpl.render('curso_detalhe.html', {'curso': curso,'_path':'/'})