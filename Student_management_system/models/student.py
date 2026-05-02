from odoo import fields, models, api

class Student(models.Model):
    _name = 'student.deatils'
    _description = 'Student Details'

    name = fields.Char("Name")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Gender")
    age = fields.Date("Age")
    phone = fields.Char("Phone")
    email = fields.Char("Email")
    address = fields.Char("Address")
    parent_name = fields.Char("Parent Name")
    parent_phone = fields.Char("Parent Phone")
    emergency_contact = fields.Char("Emergency Contact")
    course = fields.Char("Course")
    year = fields.Selection([
        ('1', '1st Year'),
        ('2', '2nd Year'),
        ('3', '3rd Year'),
        ('4', '4th Year')
    ], string="Year")

    division = fields.Char("Division")
    roll_no = fields.Integer("Roll Number")
    admission_date = fields.Date(default=fields.Date.today)
    percentage = fields.Float("Percentage")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('admitted', 'Admitted'),
        ('passed', 'Passed'),
    ], default="draft")

    def action_admit(self):
        for rec in self:
            rec.state = 'admitted'

    def action_pass(self):
        for rec in self:
            rec.state = 'passed'

    def action_reset(self):
        for rec in self:
            rec.state = 'draft'