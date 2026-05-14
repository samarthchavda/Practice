from odoo import api, fields, models

class QuotationLine(models.Model):
    _name = 'quotation.line'
    _description = 'Quotation Line'

    quotation_id = fields.Many2one(
        'sales.quotation',
        string="Quotation",
        ondelete="cascade"
    )

    product_id = fields.Many2one(
        'sales.product',
        string="Product",
        required=True
    )

    quantity = fields.Integer(string="Quantity", default=1)
    price = fields.Float(string="Price")

    subtotal = fields.Float(
        string="Subtotal",
        compute="_compute_subtotal",
        store=True
    )

    @api.depends('quantity', 'price')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.price = self.product_id.price