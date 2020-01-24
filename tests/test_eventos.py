# -*- coding: utf-8 -*-
from odoo.tests import TransactionCase

class test_eventos(TransactionCase):

    def test_validar_unico_false(self):
        esperado = False
        obtenido = self.env['asw.eventos'].es_fecha_valida('2020-01-24')

        self.assertEqual(esperado, obtenido)
    
    def test_validar_unico_true(self):
        esperado = True
        obtenido = self.env['asw.eventos'].es_fecha_valida('2020-01-01')
        
        self.assertEqual(esperado, obtenido) 