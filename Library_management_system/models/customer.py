from odoo import api, fields, models

class Customer(models.Model):
    _name = 'library.customer'
    _description = 'Customers library'

    name = fields.Char(string="Customer Name", required=True)
    # book_ids = fields.Many2many(
    #     'library.data',
    #     string="Books",
    # )

    book_count = fields.Integer(string="Book Count",compute="_compute_book_count")

    @api.depends()
    def _compute_book_count(self):
        for rec in self:
            rec.book_count = self.env['issue.book'].search_count([
                ('customer_id', '=', rec.id)
            ])

    def action_open_issues(self):
        self.ensure_one()

        return {
            'type': 'ir.actions.act_window',
            'name': 'Book Issues',
            'res_model': 'issue.book',
            'view_mode': 'list,form',
            'domain': [('customer_id', '=', self.id)],
            'context': {'default_customer_id': self.id},
        }