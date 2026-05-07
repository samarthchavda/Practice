from odoo import fields, models,api

class Order(models.Model):
    _name = 'sales.order'
    _rec_name = 'order_number'
    _description = 'Sales Order'

    order_number = fields.Char(string="Order Number", required=True, copy=False, readonly=True, default='New')
    date = fields.Date(string="date")
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

    @api.depends('order_line_ids.subtotal')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(order.order_line_ids.mapped('subtotal'))
            # with gst add total prodct
            # subtotal = sum(order.order_line_ids.mapped('subtotal'))
            # gst = subtotal * 18 / 100
            # order.total_amount = subtotal + gst

# use for a sequence increment automatic number
    @api.model_create_multi
    def create(self, vals_list):
        last_order = self.search(
            [('order_number', 'like', 'S%')],
            order="id desc",
            limit=1
        )
        if last_order and last_order.order_number:
            number_part = last_order.order_number.replace("S", "")
            next_number = int(number_part) + 1
        else:
            next_number = 1
        for vals in vals_list:
            if vals.get("order_number", "New") == "New":
                vals["order_number"] = "S" + str(next_number).zfill(3)
                next_number += 1
        return super().create(vals_list)


    def action_order_confirm(self):
        for order in self:
            order.state = 'confirmed'

            if not order.delivery_ids:
                self.env['sales.delivery'].create({  #running like a query
                    'order_id': order.id,
                    'delivery_name': 'DEL-' + order.order_number,
                    'delivery_date': fields.Date.today(),
                    'status': 'draft',
                })
            if not order.invoice_ids:
                self.env['sales.invoice'].create({
                    'order_id': order.id,
                    'invoice_number': 'INV-' + order.order_number,
                    'invoice_date': fields.Date.today(),
                    'amount': order.total_amount,
                    'status': 'draft',
                })

    def action_order_cancel(self):
        for order in self:
            order.state = 'cancel'
    def action_order_reset(self ):
        for order in self:
            order.state = 'draft'

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancel', 'Cancelled')
    ], default='draft')

    # smart button logic and their classes
    delivery_count = fields.Integer(string="Delivery Count",default=0,compute='_compute_delivery_count')
    order_invoice = fields.Char(string="Order Invoice",default=0,compute='_compute_invoice_count')
    order_quotations = fields.Char(string="Order Quotations")
    order_payment = fields.Char(string="Order Payment")

    def action_order_delivery(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Deliveries',
            'res_model': 'sales.delivery',
            'view_mode': 'list,form',
            'domain': [('order_id', '=', self.id)],
            'context': {'default_order_id': self.id},
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
    def action_order_quotations(self):
        pass
    def action_order_payment(self):
        pass

    # reversed for salesdelivery class
    delivery_ids = fields.One2many(
        'sales.delivery',
        'order_id',
        string="Deliveries",
    )
    @api.depends('delivery_ids')
    def _compute_delivery_count(self):
        for order in self:
            order.delivery_count = len(order.delivery_ids)

    # invoice page logic with one2many
    invoice_ids = fields.One2many(
        'sales.invoice',
        'order_id',
        string="Invoices"
    )
    @api.depends('invoice_ids')
    def _compute_invoice_count(self):
        for order in self:
            order.order_invoice = len(order.invoice_ids)

    quotation_id = fields.Many2one(
        'sales.quotation',
        string="Quotations",
        ondelete='cascade',
    )

    customer_name = fields.Char(string="Customer Name")