from odoo import fields, models,api
from odoo.exceptions import ValidationError

class OrderLine(models.Model):
    _name = 'order.line'
    _description = 'Order Line'
    _rec_name = 'order_id'

    # product_name = fields.Char(string='Product Name')
    quantity = fields.Integer(string='Quantity')
    price = fields.Float(string='Price')

    order_id = fields.Many2one(
        'sales.order',
        string="Order",
        ondelete='cascade',
    )

    subtotal = fields.Float(
        string="subtotal",
        compute='_compute_subtotal'
    )

    @api.depends('quantity','price')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price

    # product details catch
    product_id = fields.Many2one(
        'sales.product',
        string='product',
        required=True,
    )

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.price = self.product_id.price

    @api.constrains('quantity')
    def _check_quantity(self):
        for line in self:
            if line.quantity <= 0:
                raise ValidationError("Quantity must be greater than 0.")