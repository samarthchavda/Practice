from odoo import models,fields

class EmpManagement(models.Model):
    _name = 'emp.data' #database name
    _description = "employee data"

    name = fields.Char(string="name")
    phone_no = fields.Char(string="phone_no")
    birth_date = fields.Char(string="birth_date")
    salary = fields.Char(string="salary")