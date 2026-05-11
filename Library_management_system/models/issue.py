from odoo import fields, models
from odoo.exceptions import UserError

class Issue(models.Model):
    _name = 'issue.book'
    _description = 'Books'
    _rec_name = 'book_id'

    customer_id = fields.Many2one(
        'library.customer',
        string='Customer',
        required=True,
        )
    book_id = fields.Many2one(
        'library.data',
        string='Book',
        required=True,
    )
    issue_date = fields.Datetime(
        string='Issue Date',
        default=fields.Date.today,
    )
    return_date = fields.Datetime(
        string='Return Date',
    )

    status = fields.Selection([
        ('issued', 'Issued'),
        ('returned', 'Returned')
    ],default='issued')

    def action_return_book(self):
        for rec in self:
           if rec.status == 'returned':
               raise UserError("this book is returned")
           rec.status = 'returned'
           rec.return_date = fields.Date.today()