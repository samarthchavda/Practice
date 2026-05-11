from odoo import fields, models

class Sports(models.Model):
    _name = 'student.sports'
    _description = 'Student Sports'

    name = fields.Char(string="Name", required=True)

    student_ids = fields.Many2many(
        'student.deatils',
        #'table name',
        #'column name',
        #'column name 2',
        string="Students",
    )
