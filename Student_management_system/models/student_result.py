from odoo import models, fields

class StudentResult(models.Model):
    _name = 'student.result'

    student_id = fields.Many2one(
        'student.deatils',
        string="Student Details",
        required=True
    )

    semester = fields.Selection([
        ('1','semester 1'),
        ('2', 'semester 2'),
        ('3', 'semester 3'),
        ('4', 'semester 4'),
    ],string="Semester",required=True)

    subject_1 = fields.Char(string="Subject 1", required=True)
    marks_1 = fields.Float(string="Marks 1", required=True)

    subject_2 = fields.Char(string="Subject 2", required=True)
    marks_2 = fields.Float(string="Marks 2", required=True)
