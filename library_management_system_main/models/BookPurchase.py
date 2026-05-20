from odoo import api, fields, models
from odoo.exceptions import ValidationError

class BookPurchase(models.Model):
    _name = 'books.purchase'
    _description = 'Books'
    _rec_name = 'member_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    member_id = fields.Many2one(
        'lib.member',
        string='Member',
        required=True,
    )
    purchase_date = fields.Date(string="Purchase Date", default=fields.Date.today)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], default='draft')


    def action_buy_book(self):
        for rec in self:
            if not rec.purchase_line_ids:
                raise ValidationError("Please add at least one purchase line.")

            for line in rec.purchase_line_ids:
                if line.quantity <= 0:
                    raise ValidationError("Quantity must be greater than 0.")

                if line.book_id.quantity < line.quantity:
                    raise ValidationError(f"Not enough stock for {line.book_id.b_name}.")

                line.book_id.quantity -= line.quantity

            if rec.state == 'done':
                raise ValidationError("This purchase is already done.")

            rec.state = 'done'



    def action_cancel(self):
        for rec in self:
            if rec.state == 'done':
                for line in rec.purchase_line_ids:
                    line.book_id.quantity += line.quantity

            rec.state = "cancel"


    invoices_number = fields.Char(string="Number of Invoices",copy=False,readonly=True,default="New")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('invoices_number') or vals.get('invoices_number') == "New":
                vals['invoices_number'] = self.env['ir.sequence'].next_by_code('books.purchase') or 'New'

        return super().create(vals_list)

    def write(self, vals):
        blocked_fields = [
            'invoices_number',
            'member_id',
            'book_id',
            'purchase_date',
            'state',
            'quantity',
        ]
        for rec in self:
           if rec.state == 'done':
               for fields in blocked_fields:
                   if fields in vals:
                       raise ValidationError("You cannot update book purchase details after it is done.")
        return super().write(vals)

    purchase_line_ids = fields.One2many(
        'purchase.line',
        'purchase_id',
        string='Purchase Lines'
    )

    total_amount = fields.Float(
        string="Total Amount",
        compute='_compute_total_amount',
        store=True,
        )

    gst_amount = fields.Float(
        string="GST Amount",
        compute='_compute_total_amount',
        store=True,
    )

    grand_total = fields.Float(
        string="Grand Amount",
        compute='_compute_total_amount',
        store=True,
    )

    @api.depends('purchase_line_ids.subtotal')
    def _compute_total_amount(self):
        for rec in self:
            rec.total_amount = sum(rec.purchase_line_ids.mapped('subtotal'))
            rec.gst_amount = rec.total_amount * 0.18
            rec.grand_total = rec.total_amount + rec.gst_amount
