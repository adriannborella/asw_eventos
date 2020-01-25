# -*- coding: utf-8 -*-
from odoo import models, fields, api

class calendar_event(models.Model):
    _inherit = 'calendar.event'
    
    eventos_ids = fields.One2many(
        string='eventos',
        comodel_name='asw.eventos',
        inverse_name='event_id',
    )
    