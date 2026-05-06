from odoo import models, fields, api

class StudentResult(models.Model):
    _name = 'student.result'
    _rec_name = "student_id"

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

    total_marks = fields.Float(
        string="Total Marks",
        compute="_compute_total_marks",
        store=True
    )

    percentage = fields.Float(
        string="Percentage",
        compute="_compute_percentage",
        store=True
    )

    status = fields.Selection([
        ('pass','Pass'),
        ('fail','Fail'),
    ], string='Status',compute='_compute_status',store=True)

    @api.depends('marks_1', 'marks_2')
    def _compute_total_marks(self):
        for rec in self:
            rec.total_marks = rec.marks_1 + rec.marks_2

    @api.depends('total_marks')
    def _compute_percentage(self):
        for rec in self:
            rec.percentage = (rec.total_marks / 200) * 100

    @api.depends('percentage')
    def _compute_status(self):
        for rec in self:
            rec.status = 'pass' if rec.percentage >= 35 else 'fail'