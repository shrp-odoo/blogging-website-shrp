#-*- coding: utf-8 -*-
#Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Blogging Website',
    'category': 'Website/Blogging',
    'description': 'This is a blogging website in which we can create, read, delete and update the blogs',
    'summary': 'Blogging Website',
    'installable': True,
    'application': True,
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/custom_blogs_views.xml',
        'views/custom_blogs_tags.xml',
        'views/custom_blogs_comment.xml',
        'views/custom_blogs_menus.xml',
        'views/author_view.xml',
    ],
    'license': 'OEEL-1',
    'version': '1.0',
}
