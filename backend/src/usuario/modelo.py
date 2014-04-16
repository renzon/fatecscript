# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb


class Usuario(ndb.Model):
    google_id = ndb.StringProperty()
    nome = ndb.StringProperty()
    email = ndb.StringProperty()

    @classmethod
    def query_encontrar_por_google_id(cls, google_id):
        return cls.query(cls.google_id == google_id)

