from odoo import fields, models

class Product(models.Model):
    _name = 'sales.product'
    _description = 'Product Details'

    name = fields.Char(string="Product Name")
    price = fields.Float(string="Price")
    category = fields.Selection([
        ('electronics', 'Electronics'),
        ('fashion', 'Fashion'),
        ('grocery', 'Grocery'),
        ('furniture', 'Furniture'),
    ],string="Product Category")

    customer_ids = fields.Many2many(
        "sales.customer",
        "sales_customer_product_rel",
        "product_id",
        "customer_id",
        string="Customers"
    )