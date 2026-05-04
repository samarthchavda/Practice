from odoo import fields, models

class Student(models.Model):
    _name = 'student.deatils'
    _description = 'Student Details'

    name = fields.Char("Name", required=True)
    roll_no = fields.Integer("Roll Number")
    phone = fields.Char("Phone")
    student_active =fields.Boolean("Active", default=True)
    nationality = fields.Selection([
        ('indian','Indian'),
        ('non_indian','Non Indian')
    ],string="Nationality",required=True)
    other = fields.Char("Other")

    result_ids = fields.One2many(
        'student.result',
        'student_id',
        string="Student Results"
    )