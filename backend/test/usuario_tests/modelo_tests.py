# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from usuario.modelo import Usuario


class BuscaGoogleIdTests(GAETestCase):
    def test_busca_vazia(self):
        query=Usuario.query_encontrar_por_google_id('123')
        self.assertListEqual([], query.fetch())

    def test_busca_nao_vazia(self):
        usuario=Usuario(google_id='123')
        usuario.put()
        query=Usuario.query_encontrar_por_google_id('123')
        self.assertListEqual([usuario], query.fetch())