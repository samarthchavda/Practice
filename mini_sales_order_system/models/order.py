from odoo import fields, models,api

class Order(models.Model):
    _name = 'sales.order'
    _description = 'Sales Order'

    order_number = fields.Char(string="Order Number", required=True, copy=False, readonly=True)
    date = fields.Date(string="date")

    order_line_ids = fields.One2many(
        'order.line',
        'order_id',
        string="Order Lines"
    )

    total_amount = fields.Float(
        string="Total Amount",
        compute="_compute_total_amount",
        readonly=True
    )

    @api.depends('order_line_ids.subtotal')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(order.order_line_ids.mapped('subtotal'))
            # with gst add total prodct
            # subtotal = sum(order.order_line_ids.mapped('subtotal'))
            # gst = subtotal * 18 / 100
            # order.total_amount = subtotal + gst
