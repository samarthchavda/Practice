from odoo import fields, api, models
from odoo.exceptions import ValidationError


class Issue(models.Model):
    _name = 'lib.issue'
    _description = 'Issue'

    member_id = fields.Many2one('lib.member', string='Member', required=True)

    book_id = fields.Many2one(
        'lib.books.data',
        string='Book',
        required=True,
        domain="[('quantity', '>', 0)]"
    )

    issue_date = fields.Datetime(string="Issue Date", default=fields.Datetime.now)
    return_date = fields.Datetime(string="Return Date")

    fine_amount = fields.Float(
        string="Fine Amount",
        compute='_compute_fine',
        store=True,
    )

    late_days = fields.Integer(
        string="Late Days",
        compute='_compute_fine',
        store=True,
    )

    status = fields.Selection([
        ('draft', 'Draft'),
        ('issued', 'Issued'),
        ('returned', 'Returned'),
    ], default='draft')

    @api.depends('return_date', 'status')
    def _compute_fine(self):
        for rec in self:
            rec.fine_amount = 0
            rec.late_days = 0

            if rec.return_date and rec.status == 'issued':
                today = fields.Date.today()
                return_date = rec.return_date.date()

                if today > return_date:
                    rec.late_days = (today - return_date).days
                    rec.fine_amount = rec.late_days * 10

    def action_issue_book(self):
        for rec in self:
            if rec.status != 'draft':
                raise ValidationError("Only draft records can be issued.")

            if rec.book_id.quantity <= 0:
                raise ValidationError("This book is out of stock.")

            rec.book_id.quantity -= 1
            rec.status = 'issued'

    def action_return_book(self):
        for rec in self:
            if rec.status != 'issued':
                raise ValidationError("Only issued books can be returned.")

            rec.book_id.quantity += 1
            rec.status = 'returned'