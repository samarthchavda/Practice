from odoo import models,fields

class EmpManagement(models.Model):
    _name = 'emp.master'
    
    name = fields.Char("Name")
    phone_no = fields.Char("Phone No")
    birth_date = fields.Date("Birth Date")
    gross_sal = fields.Float("Gross Salary")