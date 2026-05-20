from odoo import api, fields, models
from odoo.exceptions import UserError

class Payment(models.Model):
    _name = "sales.payment"
    _description = "Sales Order Payment"
    _rec_name = "payment_number"

    payment_number = fields.Char(string="Payment Number",required=True,default="New",readonly=True,copy=False)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('payment_number','New') == 'New':
                vals['payment_number'] = self.env['ir.sequence'].next_by_code('sales.payment')
        return super().create(vals_list)

    order_id = fields.Many2one(
        'sales.order',
        string="Sales Order",
        required=True,
        ondelete="cascade",
        domain=[('state', '=', 'confirmed')],
    )

    @api.constrains('order_id')
    def _check_order_not_cancelled(self):
        for payment in self:
            if payment.order_id and payment.order_id.state == 'cancel':
                raise UserError("You cannot create payment for cancelled order.")

    payment_date = fields.Date(
        string="Payment Date",
        default=fields.Date.today
    )

    amount = fields.Float(
        string="Amount",
        related="order_id.grand_total",
        readonly=True,
    )

    status = fields.Selection([
        ("draft", "Draft"),
        ("paid", "Paid"),
        ("cancel", "Cancelled")
    ], default="draft")

    def action_paid(self):
        for payment in self:
            order = payment.order_id

            if order.state != 'confirmed':
                raise UserError("Only confirmed order payment can be paid.")

            if not order.stock_deducted:
                for line in order.order_line_ids:
                    if line.quantity > line.product_id.stock_qty:
                        raise UserError(
                            f"Not enough stock for {line.product_id.name}. "
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

    def action_cancel(self):
        for payment in self:
            payment.status = "cancel"