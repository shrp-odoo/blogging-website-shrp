#-*- coding: utf-8 -*-

from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    details = fields.One2many("custom.blog","author_ids")
    