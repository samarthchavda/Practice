from odoo import models, fields, api

class Author(models.Model):
    _name = 'library.author'
    _description = 'Library Author data'

    auth_name = fields.Char(string="Author Name", required=True)

    book_id = fields.One2many(
        'library.data',
        'author_id',
        string="Books",
    )

    book_count = fields.Integer(
        string="Book Count",
        compute='_compute_count',
    )

    @api.depends('book_id')
    def _compute_count(self):
        for rec in self:
            rec.book_count = len(rec.book_id)