from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"


    # revers of many2one (that id is use to where we put a buyer details that
    # time to store for perticular buyer data for that property)
    offer_id = fields.One2many(
        'estate.property.offer',
        'property_id',
        string="Offers",
    )
    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available From")
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    active = fields.Boolean(string="Active", default=True)
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection(
        [
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ],
        string="Garden Orientation",
    )
    # page2
    address = fields.Char(string="Address")
    area = fields.Char(string="Area")
    city = fields.Char(string="City")
    pincode = fields.Char(string="Pincode")

    buyer_name = fields.Char(string="Buyer Name", readonly=True)

    # button login which is show in header
    def action_offer_received(self):
        for rec in self:
            rec.state = 'offer_received'
    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'

    state = fields.Selection([
        ('new','New'),
        ('offer_received','Offer Received'),
        ('sold','Sold'),
        ('cancelled','Cancelled'),
    ], string="status", default="new")


    # smart button added like crm
    meeting_count = fields.Integer(string="Meeting Count", compute="_compute_count")
    offer_count = fields.Integer(string="Offer Count", compute="_compute_count")
    rental_count = fields.Integer(string="Rental Count", compute="_compute_count")

    def _compute_count(self):
        for rec in self:
            rec.meeting_count = 0
            rec.offer_count = len(rec.offer_id)
            rec.rental_count = 0

    def action_view_meetings(self):
        pass

    def action_view_offers(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Offers',
            'res_model': 'estate.property.offer',
            'view_mode': 'list,form',
            'domain': [('property_id', '=', self.id)],
            'context': {'default_property_id': self.id},
        }
    def action_view_rental(self):
        pass

    # logic of buyer name that can show in property list




