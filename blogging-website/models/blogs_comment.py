#-*- coding: utf-8 -*-

from odoo import models, fields

class BlogComment(models.Model):
    _name = 'custom.blog.comment'
    _description = 'Blog Comments'

    comment = fields.Char()
    custom_blog_id = fields.Many2one('custom.blog', string='Blog Post')
