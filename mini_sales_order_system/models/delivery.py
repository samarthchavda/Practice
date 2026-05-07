from odoo import api, fields, models

class SalesDelivery(models.Model):
    _name = 'sales.delivery'
    _description = 'Sales Delivery'
    _rec_name = 'delivery_name'

    order_id = fields.Many2one(
        'sales.order',
        string="Order",
    )

    delivery_name = fields.Char(string="Delivery Reference",required=True)
    delivery_date = fields.Date(string="Delivery Date")
    status = fields.Selection([
        ('draft', 'Draft'),
        ('ready', 'Ready'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ],default='draft')

    # header button function
    def action_ready(self):
        self.status = 'ready'

    def action_done(self):
        self.status = 'done'

    def action_cancel(self):
        self.status = 'cancel'