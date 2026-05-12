from odoo import fields, models

class Skill(models.Model):
    _name = 'hospital.skill'
    _description = 'Hospital Skill'

    name = fields.Char(string="Skill Name", required=True)