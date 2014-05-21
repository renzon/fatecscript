# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest


class SomaTests(unittest.TestCase):
    def setUp(self):
        print ('setup')

    def test_funcao_soma(self):
        resultado=1+2
        self.assertEqual(3,resultado)
        print 'soma'

    def test_blah(self):
        print 'blah'

    def tearDown(self):
        print 'tear down'

if __name__=='__main__':
    unittest.main()