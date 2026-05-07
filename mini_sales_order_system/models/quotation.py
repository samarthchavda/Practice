from odoo import api, fields, models

class Quotation(models.Model):
    _name = 'sales.quotation'
    _description = 'Sales Quotation'

    quotation_number = fields.Char(string='Quotation', required=True)
    customer_name = fields.Char(string='Customer Name')
    quotation_date = fields.Date(string='Date of Quotation')
    amount = fields.Float(string='Amount')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('confirmed', 'Confirmed'),
        ('cancel', 'Cancelled'),
    ],default='draft')

    def action_sent(self):
        self.status = 'sent'

    def action_confirmed(self):
        for quotation in self:
            quotation.status = 'confirmed'

            if not quotation.order_id:
                order = self.env['sales.order'].create({
                    'date': quotation.quotation_date,
                    'quotation_id': quotation.id,
                    'customer_name': quotation.customer_name,
                })

                quotation.order_id = order.id


    def action_cancel(self):
        self.status = 'cancel'

    order_id = fields.Many2one(
        'sales.order',
        string="Created Order",
        readonly=True,
        ondelete='cascade',

    )
