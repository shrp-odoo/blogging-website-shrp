from odoo import fields, models, api, Command

class EstateAddOffer(models.TransientModel):
    _name = 'blogs.add.offer'
    _description = "Add offer to blogs"
    
    comment = fields.Char(string='Blogs Comments', required=True)
    blogs_comment = fields.Many2one('custom.blog')

    def action_like_selected_blogs(self):
        active_ids = self.env.context.get('active_ids')
        blogs = self.env['custom.blog'].browse(active_ids)
        blogs.write (
            {
                'comments_ids' : [
                    Command.create({
                        "comment" : self.comment
                    })
                ]
            }
        )
