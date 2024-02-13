#-*- coding: utf-8 -*-
from odoo import models, fields

class User(models.Model):
    _name = 'custom.user'
    _description = 'property of user'

    name = fields.Char(string='Enter your Name', required=True)
    email = fields.Char(string='Enter your Email', required=True)
    password = fields.Char(string='Enter your password', required=True)
