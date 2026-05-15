from odoo import fields, models,api
from odoo.exceptions import UserError


class Order(models.Model):
    _name = 'sales.order'
    _rec_name = 'order_number'
    _description = 'Sales Order'

    order_number = fields.Char(
        string="Order Number",
        required=True,
        copy=False,
        readonly=True,
        default="New"
    )
    date = fields.Date(string="date")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('order_number') or vals.get('order_number') == 'New':
                vals['order_number'] = self.env['ir.sequence'].next_by_code(
                    'sales.order.sequence'
                ) or 'New'

        return super().create(vals_list)

    # for order lines one2many reverse process because of showinng in list in order page
    order_line_ids = fields.One2many(
        'order.line',
        'order_id',
        string="Order Lines"
    )
    total_amount = fields.Float(
        string="Total Amount",
        compute="_compute_total_amount",
        readonly=True
    )

    # reversed for salesdelivery class
    delivery_ids = fields.One2many(
        'sales.delivery',
        'order_id',
        string="Deliveries",
        ondelete='cascade',
    )

    # invoice page logic with one2many
    invoice_ids = fields.One2many(
        'sales.invoice',
        'order_id',
        string="Invoices"
    )

    def action_order_confirm(self):
        for order in self:
            for line in order.order_line_ids:
                if line.quantity > line.product_id.stock_qty:
                    raise UserError(
                        f"Not enough stock for {line.product_id.name}. "
                        f"Available: {line.product_id.stock_qty}"
                    )

            if not order.order_line_ids:
                raise UserError("please add at least one order line")

            order.state = 'confirmed'

            if not order.invoice_ids:
                self.env['sales.invoice'].create({
                    'order_id': order.id,
                    'invoice_number':self.env['ir.sequence'].next_by_code('sales.invoice'),
                    'invoice_date': fields.Date.today(),
                    'amount': order.total_amount,
                    'status': 'draft',
                })

    def action_order_cancel(self):
        for order in self:
            if order.state != 'confirmed':
                raise UserError("please add at least one order line")
            if order.payment_ids.filtered(lambda p: p.status == 'paid'):
                raise UserError("You cannot cancel this order because payment is already paid.")

            order.state = 'cancel'

    def action_order_reset(self ):
        for order in self:
            if order.payment_ids.filtered(lambda p: p.status == 'paid'):
                raise UserError("Do not rest this order because payment is already paid.")
            order.state = 'draft'

    has_paid_payment = fields.Boolean(string="Has Payment",compute='_compute_paid_payment')
    stock_deducted = fields.Boolean(string="Stock Deducted", default=False)

    @api.depends('payment_ids.status')
    def _compute_paid_payment(self):
        for order in self:
            order.has_paid_payment = any(
                payment.status == 'paid'
                for payment in order.payment_ids
            )

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancel', 'Cancelled')
    ], default='draft')

    # smart button logic and their classes
    delivery_count = fields.Integer(string="Delivery Count",default=0,compute='_compute_delivery_count')

    @api.depends('delivery_ids')
    def _compute_delivery_count(self):
        for order in self:
            order.delivery_count = len(order.delivery_ids)

    order_invoice = fields.Integer(string="Order Invoice",default=0,compute='_compute_invoice_count')

    @api.depends('invoice_ids')
    def _compute_invoice_count(self):
        for order in self:
            order.order_invoice = len(order.invoice_ids)

    order_payment = fields.Integer(string="Order Payment",default=0,compute='_compute_payment_count')

    @api.depends('payment_ids')
    def _compute_payment_count(self):
        for order in self:
            order.order_payment = len(order.payment_ids)

    # order_quotations = fields.Char(string="Order Quotations")

    def action_order_delivery(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Deliveries',
            'res_model': 'sales.delivery',
            'view_mode': 'list',
            'domain': [('order_id', '=', self.id)],
            'context': {'create': False},
        }

    def action_order_invoice(self):
        self.ensure_one() #each every record to run that
        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoices',
            'res_model': 'sales.invoice',
            'view_mode': 'list,form',
            'domain': [('order_id', '=', self.id)],
            'context': {'default_order_id': self.id},
        }
    # def action_order_quotations(self):
    #     pass
    def action_order_payment(self):
        self.ensure_one()
        if self.state == 'cancel':
            raise UserError("You cannot create payment for cancelled order.")
        return {
            'type': 'ir.actions.act_window',
            'name': 'Payments',
            'res_model': 'sales.payment',
            'view_mode': 'list,form',
            'domain': [('order_id', '=', self.id)],
            'context': {'default_order_id': self.id},
        }

    quotation_id = fields.Many2one(
        'sales.quotation',
        string="Quotations",
        ondelete='cascade',
    )


    customer_name = fields.Char(string="Customer Name")

    payment_ids = fields.One2many(
        'sales.payment',
        'order_id',
        string="Payments",
    )

    gst_amount = fields.Float(string="GST 18%",compute='_compute_total_amount',store=True)
    grand_total = fields.Float(string="Grand Total",compute='_compute_total_amount',store=True)

    @api.depends('order_line_ids.subtotal')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(order.order_line_ids.mapped('subtotal'))
            order.gst_amount = order.total_amount * 0.18
            order.grand_total = order.total_amount + order.gst_amount

