# -*- coding: utf-8 -*-

from odoo import http

class Blogging(http.Controller):

    @http.route('/blogs', auth='public', type='http', website=True)
    def index(self):
        blogs = http.request.env['custom.blog'].search([('status', 'not in', ['draft'])])
        return http.request.render('blogging-website.website_blogs_page', {
            'blogs': blogs
        })

    @http.route('/blogs/<string:title>/', auth='public', type='http', website=True)
    def blogs_details(self, title):
        blog_details = http.request.env['custom.blog'].search([('title', '=', title)])
        return http.request.render('blogging-website.blogs_details', {
            'blogs': blog_details
        })
