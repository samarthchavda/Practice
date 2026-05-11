from odoo import api, fields, models

class Payment(models.Model):
    _name = "sales.payment"
    _description = "Sales Order Payment"
    _rec_name = "payment_number"

    payment_number = fields.Char(
        string="Payment Number",
        required=True,
        default="New",
        readonly=True,
        copy=False
    )

    order_id = fields.Many2one(
        'sales.order',
        string="Sales Order",
        required=True,
        ondelete="cascade",
    )

    payment_date = fields.Date(
        string="Payment Date",
        default=fields.Date.today
    )

    amount = fields.Float(
        string="Amount",
        related="order_id.total_amount",
        readonly=True,
    )

    status = fields.Selection([
        ("draft", "Draft"),
        ("paid", "Paid"),
        ("cancel", "Cancelled")
    ], default="draft")

    @api.model_create_multi
    def create(self, vals_list):
        last_payment = self.search(
            [('payment_number', 'like', 'P%')],
            order="id desc",
            limit=1
        )

        if last_payment and last_payment.payment_number:
            number_part = last_payment.payment_number[1:]
            next_number = int(number_part) + 1
        else:
            next_number = 1

        for vals in vals_list:
            if vals.get("payment_number", "New") == "New":
                vals["payment_number"] = "P" + str(next_number).zfill(3)
                next_number += 1

        return super().create(vals_list)

    def action_paid(self):
        for payment in self:
            payment.status = "paid"

            order = payment.order_id
            if order.invoice_ids:
                order.invoice_ids.write({
                    'status': 'paid'
                })
            if order and not order.delivery_ids:
                self.env['sales.delivery'].create({
                    'order_id': order.id,
                    'delivery_name': 'DEL-' + order.order_number,
                    'delivery_date': fields.Date.today(),
                    'status': 'draft',
                })

    def action_cancel(self):
        for payment in self:
            payment.status = "cancel"