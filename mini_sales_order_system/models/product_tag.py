from odoo import fields,models

class ProductTag(models.Model):
    _name = 'sales.product.tag'
    _description = "Product Tag"

    name = fields.Char(string="Tag name",required=True)