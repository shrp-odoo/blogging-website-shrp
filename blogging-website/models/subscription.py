#-*- coding: utf-8 -*-
from odoo import models, fields

class blogsSubscription(models.Model) :
    _name = 'custom.blogsubscription'
    _description = 'blogs subscription'

    blog_id = fields.Many2one('custom.blog', string='Blog Post', required=True)
    subscription_id = fields.Many2one('custom.user', string='Subscriber', required=True)
    subscription_date = fields.Datetime(string='Subscription Date', default=fields.Datetime.now)
