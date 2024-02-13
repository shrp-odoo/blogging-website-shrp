#-*- coding: utf-8 -*-
from odoo import models, fields

class blogs(models.Model):
    _name = 'custom.blog'
    _description = 'Custom blog description'

    title = fields.Char(string='Blogs title', required=True, default='Write a title to generate your blog')
    content = fields.Char(string='Content')
    author_id = fields.Many2one('custom.user', string='Author', required=True)
    published_date = fields.Date(string='Published Date')
    tags = fields.Many2many('custom.tag', string='Tags')
    image = fields.Image(string='Upload Images')
    likes_count = fields.Integer(string='Likes', default=0)
    dislikes_count = fields.Integer(string='Dislikes', default=0)
