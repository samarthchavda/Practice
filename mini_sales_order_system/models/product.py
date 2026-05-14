from odoo import fields, models,api
from odoo.exceptions import ValidationError

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
        ('food', 'Food'),
    ],string="Product Category")

    customer_ids = fields.Many2many(
        "sales.customer",
        "sales_customer_product_rel",
        "product_id",
        "customer_id",
        string="Customers"
    )

    @api.constrains('price')
    def _check_price(self):
        for line in self:
            if line.price <= 0:
                raise ValidationError("price could not be less than 0")

    @api.constrains('name')
    def _check_name(self):
        for rec in self:
            existing = self.search([
                ('name','=', rec.name),
                ('id','!=',rec.id),
            ])
            if existing:
                raise ValidationError("name already exists")

    tag_ids = fields.Many2many(
        'sales.product.tag',
        string="product Tags",
    )