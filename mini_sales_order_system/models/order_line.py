from odoo import fields, models,api

class OrderLine(models.Model):
    _name = 'order.line'
    _description = 'Order Line'

    product_name = fields.Char(string='Product Name')
    quantity = fields.Integer(string='Quantity')
    price = fields.Float(string='Price')

    order_id = fields.Many2one(
        'sales.order',
        string="Order"
    )

    subtotal = fields.Float(
        string="subtotal",
        compute='_compute_subtotal'
    )

    @api.depends('quantity','price')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price
            
