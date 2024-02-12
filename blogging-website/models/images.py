#-*- coding: utf-8 -*-
from odoo import models, fields

class blogsImage(models.Model):
    _name = "custom.image"
    _description = "custom images of blogs"

    name = fields.Char(string='Name',required=True)
    image = fields.Binary(string='Image', required=True)
    blog_id = fields.Many2one('custom.blog',string='Blog',required=True)
