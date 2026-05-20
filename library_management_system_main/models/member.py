from email.policy import default

from odoo import fields, models,api

class Member(models.Model):
    _name = 'lib.member'
    _description = 'Library Member'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    contact_no = fields.Char(string="Contact Number")
    city = fields.Char(string="City")
    purchase_count = fields.Integer(
        string="Purchase Count",
        compute='_compute_purchase_count',
    )
    member_number = fields.Char(
        string="Member Number",
        required=True,
        readonly=True,
        copy=False,
        default="New"
        )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('member_number') or vals.get('member_number') == 'New':
                vals['member_number'] = self.env['ir.sequence'].next_by_code('lib.member') or 'New'

        return super().create(vals_list)

    def _compute_purchase_count(self):
        for member in self:
            member.purchase_count = self.env['books.purchase'].search_count([
                ('member_id', '=', member.id),
            ])


    def action_open_purchase(self):
        self.ensure_one()
        return{
            'type': 'ir.actions.act_window',
            'name':'Book Purchase',
            'res_model': 'books.purchase',
            'view_mode': 'list,form',
            'domain': [('member_id', '=', self.id)],
            'context':{'default_member_id': self.id},
        }