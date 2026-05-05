from odoo import fields,models

class Library(models.Model):
    _name = 'library.data'
    _description = 'Books data'

    b_name = fields.Char('Book Name')
    b_description = fields.Char('Book Description')
    b_price = fields.Float('Book Price')

    author_id = fields.Many2one(
        'library.author',
        string="Author",
        required=True
    )