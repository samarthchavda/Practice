from odoo import api, fields, models

class Dashboard(models.Model):
    _name = 'sales.dashboard'
    _description = 'Sales Dashboard'
    _rec_name = 'name'

    name = fields.Char(default="sales dashboard")
    total_orders = fields.Integer(compute="_compute_dashboard")
    total_revenue = fields.Float(compute="_compute_dashboard")
    paid_payments = fields.Integer(compute="_compute_dashboard")
    pending_payments = fields.Integer(compute="_compute_dashboard")
    cancelled_orders = fields.Integer(compute="_compute_dashboard")
    deliveries = fields.Integer(compute="_compute_dashboard")
    total_products = fields.Integer(compute="_compute_dashboard")

    def _compute_dashboard(self):
        Order = self.env['sales.order']
        Payment = self.env['sales.payment']
        Delivery = self.env['sales.delivery']
        Product = self.env['sales.product']

        for rec in self:
            rec.total_orders = Order.search_count([])
            rec.total_revenue = sum(Order.search([('state', '=', 'confirmed')]).mapped('total_amount'))
            rec.paid_payments = Payment.search_count([('status', '=', 'paid')])
            rec.pending_payments = Payment.search_count([('status', '=', 'draft')])
            rec.cancelled_orders = Order.search_count([('state', '=', 'cancel')])
            rec.total_products = Product.search_count([])
            rec.deliveries = Delivery.search_count([
                ('order_id.state', '=' , 'confirmed'),
            ])
