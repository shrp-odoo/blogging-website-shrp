#-*- coding: utf-8 -*-

from odoo import  models, fields, api
from odoo.exceptions import UserError
from datetime import timedelta

class CustomBlog(models.Model):
    _name = 'custom.blog'
    _description = 'Custom blog description'

    title = fields.Char(string='Blogs title', required=True)
    content = fields.Char(string='Content', required=True)
    published_date = fields.Date(string='Published Date', required=True)
    tags = fields.Many2many('custom.tag', string='Tags')
    image = fields.Image(string='Upload Images')
    likes_count = fields.Integer(string='Likes')
    dislikes_count = fields.Integer(string='Dislikes')
    status = fields.Selection(
        selection=[("draft", "Draft"), ("save", "Save"), ("published", "Published")],
        default="draft"
    )
    category = fields.Selection(
        selection=[("industrial", "Industrial"), ("technology", "Technology"), ("other", "Other")],
        string='Category'
    )
    comments_ids = fields.One2many('custom.blog.comment', inverse_name='custom_blog_id')
    author_ids = fields.Many2one('res.users', string='Authors')
    start_date = fields.Date(string="Start Date", compute="_compute_start_end_date", store=True)
    end_date = fields.Date(string="End Date", compute="_compute_start_end_date", store=True)

    @api.depends("create_date")
    def _compute_start_end_date(self):
            for record in self:
                start_date = record.published_date
                end_date = fields.Datetime.from_string(start_date) + timedelta(days=7)
                record.start_date = start_date
                record.end_date = end_date

    @api.depends('content', 'title')
    def _compute_display_name(self):
        for record in self:
            title = record.title 
            record.display_name = title
            
    def action_save(self):
        for blog in self:
            blog.status = 'save'

    def action_published(self):
        for blog in self:
            if blog.status != 'save':
                raise UserError("Please save the blog before publishing.")
            else:
                blog.status = 'published'
    
    def action_like(self):
        for blog in self:
            blog.likes_count += 1
    
    def action_dislike(self):
        for blog in self:
            blog.dislikes_count += 1
