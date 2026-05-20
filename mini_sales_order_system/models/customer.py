from odoo import api, fields, models

class Customer(models.Model):
    _name = 'sales.customer'
    _description = 'Customer'

    name = fields.Char(string='Customer Name', required=True)
    email = fields.Char(string='Customer Email')
    phone = fields.Char(string='Customer Phone')

    product_id = fields.Many2many(
        'sales.product',
        'sales_customer_product_rel',
        'customer_id',
        'product_id',
        string='Product',
    )

    order_count = fields.Integer(compute='_compute_customer_ledger')
    total_order_amount = fields.Float(compute='_compute_customer_ledger')
    total_paid_amount = fields.Float(compute='_compute_customer_ledger')

    def _compute_customer_ledger(self):
        for customer in self:
            orders = self.env['sales.order'].search([
                ('customer_id', '=', customer.id),
            ])

            payments = self.env['sales.payment'].search([
                ('order_id.customer_id', '=', customer.id),
            ])

            customer.order_count = len(orders)
            customer.total_order_amount = sum(orders.mapped('grand_total'))
            customer.total_paid_amount = sum(payments.mapped('amount'))
    def action_open_orders(self):
        self.ensure_one()

        return {
            'type': 'ir.actions.act_window',
            'name': 'Orders',
            'res_model': 'sales.order',
            'view_mode': 'list,form',
            'domain': [('customer_id', '=', self.id)],
            'context': {'default_customer_id': self.id},
        }