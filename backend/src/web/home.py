# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from web import my_form
from tekton import router


def index(_write_tmpl):
    _write_tmpl('templates/home.html')

