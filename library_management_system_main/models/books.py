from odoo import api,fields,models

class books(models.Model):
    _name='lib.books.data'
    _description='Books'
    _rec_name = "b_name"

    book_number = fields.Char(string="Book Number", required=True,readonly=True, copy=False,default="New")
    # book_image = fields.Image(string="Book Image")
    b_name = fields.Char(string="Book Name")
    b_description = fields.Char(string="Book Description")
    b_price = fields.Float(string="Book Price")
    quantity = fields.Integer(string="Available Quantity", default=1)
    active = fields.Boolean(default=True)

    author_id = fields.Many2one(
        'lib.author.data',
        string="Author",
    )

    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            if not vals.get('book_number') or vals.get('book_number') == "New":
                vals['book_number'] = self.env['ir.sequence'].next_by_code('lib.books.data') or 'New'

            if not vals.get('barcode'):
                vals['barcode'] = self.env['ir.sequence'].next_by_code('library.book.barcode')

        return super().create(vals_list)

    barcode = fields.Char(
        string="Barcode",
        copy=False,
        readonly=True,
    )
