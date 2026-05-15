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

    stock_qty = fields.Float(string="Quantity",default=0)

    def action_paid(self):
        for payment in self:
            order = payment.order_id

            if order.state != 'confirmed':
                raise UserError("Only confirmed order payment can be paid.")

            if not order.stock_deducted:

                for line in order.order_line_ids:
                    if line.quantity > line.product_id.stock_qty:
                        raise UserError(
                            f"Not enough stock for {line.product_id.name}."
                            f"Available: {line.product_id.stock_qty}"
                        )

                for line in order.order_line_ids:
                    line.product_id.stock_qty -= line.quantity

                order.stock_deducted = True

            payment.status = "paid"

            if order.invoice_ids:
                order.invoice_ids.write({
                    'status': 'paid'
                })

            if order and not order.delivery_ids:
                self.env['sales.delivery'].create({
                    'order_id': order.id,
                    'delivery_name': self.env['ir.sequence'].next_by_code('sales.delivery'),
                    'delivery_date': fields.Date.today(),
                    'status': 'ready',
                })