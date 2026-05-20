from odoo import fields, models, api


class Dashboard(models.Model):
    _name = 'library.dashboard'
    _description = 'Library Dashboard'
    _rec_name = 'name'

    name=fields.Char(default='Dashboard')
    total_books = fields.Integer(string="Total Books", compute='_compute_dashboard_data')
    total_members = fields.Integer(string="Total Members", compute='_compute_dashboard_data')
    total_purchases = fields.Integer(string="Total Purchases", compute='_compute_dashboard_data')
    total_amount = fields.Float(string="Total Amount", compute='_compute_dashboard_data')
    low_stock_books = fields.Integer(string="Low Stock Books", compute='_compute_dashboard_data')

    @api.depends()
    def _compute_dashboard_data(self):
        for rec in self:
            rec.total_books = self.env['lib.books.data'].search_count([])
            rec.total_members = self.env['lib.member'].search_count([])
            rec.total_purchases = self.env['books.purchase'].search_count([])
            rec.low_stock_books = self.env['lib.books.data'].search_count([
                ('quantity', '<=', 2)
            ])

            purchases = self.env['books.purchase'].search([])
            rec.total_amount = sum(purchases.mapped('total_amount'))