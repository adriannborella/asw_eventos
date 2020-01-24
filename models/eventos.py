# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class asw_eventos(models.Model):
    _name = 'asw.eventos'
    _description = 'Eventos'
    
    fecha = fields.Date(string='fecha', required=True  )
    motivo = fields.Char(string='Motivo' )    
    active = fields.Boolean(string='active', default=True )
    
    state = fields.Selection(
        string='Estado',
        selection=[('b', 'Borrador'), ('c', 'Confirmado')]
    )

    @api.model
    def create(self, vals):
        # Agregar codigo de validacion aca
        self.validar_fecha(vals['fecha'])
        return super(asw_eventos, self).create(vals)
    
    def validar_fecha(self, fecha):
        if(self.es_fecha_valida(fecha)):
            raise UserError("Ya existe un evento cargado para ese dia, por favor revise la fecha")
    
    def es_fecha_valida(self, fecha):
        existe = self.env['asw.eventos'].search_count([('fecha', '=', fecha)])
        return existe > 0
    
    