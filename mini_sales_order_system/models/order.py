from odoo import fields, models,api

class Order(models.Model):
    _name = 'sales.order'
    _description = 'Sales Order'

    order_number = fields.Char(string="Order Number", required=True, copy=False, readonly=True, default="New")
    date = fields.Date(string="date")

    order_line_ids = fields.One2many(
        'order.line',
        'order_id',
        string="Order Lines"
    )

    total_amount = fields.Float(
        string="Total Amount",
        compute="_compute_total_amount"
    )

    @api.depends('order_line_ids.subtotal')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(order.order_line_ids.mapped('subtotal'))

