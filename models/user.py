# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Usuario(models.Model):
    _name = "upocubo.users"
    _description = "Upocubo User"
    _order = 'name'
    
    name = fields.Char(
        string="First name", size=60, required=True, help="Name of the user"
    )
    surname = fields.Char(
        string="Last name", size=60, required=True, help="Surname of the user"
    )
    DNI = fields.Char(string="DNI", size=9, required=True, help="DNI user")
    email = fields.Char(
        string="Email", size=60, required=True, help="Email of the user"
    )
    country_id = fields.Many2one(
        comodel_name="res.country",
        string="Country",
        required=True,
        help="Country of the user",
    )    
    password = fields.Char(
        string="Password", size=60, required=True, help="Password of the user"
    )
    photo = fields.Binary('Photo', help="Profile picture of the user")
