from odoo import fields,models,api
from odoo.exceptions import UserError

class Offer(models.Model):
    _name = 'estate.property.offer'
    _description = "Real Estate Property"

    price = fields.Float(string="offer Price")
    buyer_name = fields.Char(string="Buyer Name")
    status = fields.Selection([
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ],string="Status", default="pending")

    property_id = fields.Many2one(
        'estate.property',
        string="Property",
    )

    def action_accept_offer(self):
        for rec in self:
            already_accepted = rec.search([ #used api decoreators and orm concept
                ('property_id', '=', rec.property_id.id),
                ('status', '=', 'accepted'),
                ('id', '!=' ,rec.id),
            ])
            if already_accepted:
                raise UserError("This property already has an accepted offer.")

            # when a one offer is accept that time other offer is autmatic rejected for that property.
            rec.status = 'accepted'

            other_offers = rec.search([
                ('property_id', '=' ,rec.property_id.id ),
                ('id', '!=', rec.id),
            ])

            other_offers.write({
                'status' : 'rejected',
            })
            rec.status = 'accepted'
            rec.property_id.selling_price = rec.price
            rec.property_id.buyer_name = rec.buyer_name
            rec.property_id.state = 'sold'

    def action_reject_offer(self):
        for rec in self:
            was_accepted = rec.status == 'accepted'

            rec.status = 'rejected'
            if was_accepted:
                rec.property_id.state = 'offer_received'
                rec.property_id.buyer_name = False
                rec.property_id.selling_price = 0



