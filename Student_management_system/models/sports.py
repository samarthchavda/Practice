from odoo import fields, models

class Sports(models.Model):
    _name = 'student.sports'
    _description = 'Student Sports'

    name = fields.Char(string="Sport Name", required=True)

    student_ids = fields.Many2many(
        'student.deatils',
        'student_sports_rel',
        'sport_id',
        'student_id',
        string="Students"
    )