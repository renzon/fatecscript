# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb


class Curso(ndb.Model):
    criacao=ndb.DateTimeProperty(auto_now_add=True)
    descricao=ndb.StringProperty(default='Sem descrição')
    nome=ndb.StringProperty(required=True)