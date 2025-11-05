# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PaymentMethods(models.Model):
    
    _name = 'upocubo.metodos_pago'
    _description = 'Métodos de Pago del Usuario'

    
    name = fields.Char(
        string="Apodo del Método", 
        size=60, 
        required=True, 
        help="Un nombre para identificar este método de pago (ej. 'Visa Personal')"
    )

    tipo_metodo = fields.Selection([
        ('tarjeta', 'Tarjeta de Crédito'),
        ('paypal', 'PayPal'),
        ('applepay', 'Apple Pay')
    ], string="Tipo de Método", required=True, default='tarjeta')

 
    detalles = fields.Char(
        string="Detalles", 
        size=100, 
        help="Ej: '...4444' o 'usuario@paypal.com'"
    )

    user_id = fields.Many2one(
        'upocubo.users',
        string="Usuario", 
        required=True, 
        ondelete='cascade', #método para no dejar datos huérfanos, si se elimina un user, elimina todos sus métodos de pago#
        help="El usuario al que pertenece este método de pago"
    )