from odoo import api, fields,models

class SalesInvoice(models.Model):
    _name = "sales.invoice"
    _description = "Sales Invoice"

    order_id = fields.Many2one(
        'sales.order',
        string="Sales Order",
        required=True,
        ondelete='cascade', #delete child record automatically when parent record is delete
    )
    invoice_number = fields.Char(string="Invoice Number", required=True)
    invoice_date = fields.Date(string="Invoice Date")
    amount = fields.Float(string="Amount")

    status = fields.Selection([
        ('draft', 'Draft'),
        ('posted', 'Posted'),
        ('paid', 'Paid'),
        ('cancel', 'Cancel'),
    ],default='draft',)

    def action_post(self):
        self.status = 'posted'

    def action_paid(self):
        self.status = 'paid'

    def action_cancel(self):
        self.status = 'cancel'
