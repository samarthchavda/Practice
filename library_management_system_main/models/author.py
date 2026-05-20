from email.policy import default

from odoo import api, fields, models

class Author(models.Model):
    _name = 'lib.author.data'
    _description = 'Library Author Data'

    name = fields.Char(string="Author's Name")
    author_number = fields.Char(
        string="Author's Number",
        readonly=True,
        required=True,
        copy=False,
        default="New"
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('author_number') or vals.get('author_number') == 'New':
                vals['author_number'] = self.env['ir.sequence'].next_by_code('lib.auth.data') or 'New'

        return super().create(vals_list)

    book_ids = fields.One2many(
        'lib.books.data',
        'author_id',
        string='Books',
    )