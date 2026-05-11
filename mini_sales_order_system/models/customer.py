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