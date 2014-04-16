# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from usuario.modelo import Usuario


class Curso(ndb.Model):
    criacao=ndb.DateTimeProperty(auto_now_add=True)
    descricao=ndb.StringProperty(default='Sem descrição')
    nome=ndb.StringProperty(required=True)
    dono_key=ndb.KeyProperty(Usuario)

    @classmethod
    def query_encontrar_cursos_de_usuario(cls, key):
        return cls.query(cls.dono_key == key).order(cls.nome)