from odoo import models, fields

class blogs(models.Model):
    _name = "blogs.table"
    _description = "blogs table description"

    title = fields.Char(required=True)
    content = fields.Char()
    created_at = fields.Date()
    