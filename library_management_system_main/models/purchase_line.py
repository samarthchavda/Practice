from odoo import fields, models, api

class PurchaseLine(models.Model):
    _name = 'purchase.line'
    _description = 'Purchase Line'

    purchase_id = fields.Many2one(
        'books.purchase',
        string='Purchase Line',
    )

    book_id = fields.Many2one(
        'lib.books.data',
        string='Book',
    )
    quantity = fields.Integer(string='Quantity')
    price = fields.Float(string='Price')
    subtotal = fields.Float(string='Subtotal', compute='_compute_total',store=True)

    @api.depends('price', 'quantity')
    def _compute_total(self):
        for line in self:
            line.subtotal = line.price * line.quantity

    @api.onchange('book_id')
    def _onchange_book_id(self):
        for line in self:
            if line.book_id:
                line.price = line.book_id.b_price


