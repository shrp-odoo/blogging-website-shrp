#-*- coding: utf-8 -*-
from odoo import models, fields

class tags(models.Model):
    _name = 'custom.tag'
    _description = 'custom tags'

    name = fields.Char(string='Name', required=True)
    blogs_ids = fields.Many2many('custom.blog', string='Blogs')
