from odoo import fields,models

class Student(models.Model):
    _name = 'student.deatils'

    name = fields.Char("name")
    age = fields.Integer("age")
    phone = fields.Char("phone")