from odoo import api, fields, models

class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor details'

    name = fields.Char(string='Name', required=True)
    specialization = fields.Selection([
        ('general', 'General Physician'),
        ('cardio', 'Cardiologist'),
        ('ortho', 'Orthopedic'),
        ('neuro', 'Neurologist'),
        ('derma', 'Dermatologist'),
    ], string="Specialization", required=True)

    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    experience = fields.Char(string='Experience')
    consultation_fee = fields.Float(string='Consultation Fee', required=True)
    active = fields.Boolean(default=True)

    appointment_ids = fields.One2many(
        'hospital.appointment',
        'doctor_id',
        string='Appointments',
    )

    def action_open_appoinments(self):
        self.ensure_one()

        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'hospital.appointment',
            'view_mode': 'list,form',
            'domain': [('doctor_id', '=', self.id)],
            'context': {'default_doctor_id': self.id},
        }


    appointment_count = fields.Integer(compute='_compute_appointment_count')

    def _compute_appointment_count(self):
        for doctor in self:
            doctor.appointment_count = len(doctor.appointment_ids)

    skill_ids = fields.Many2many(
        'hospital.skill',
        string="Skills"
    )
