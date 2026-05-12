from odoo import fields, models,api
from odoo.exceptions import UserError


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _rec_name = 'appointment_number'

    appointment_number = fields.Char(string="Appointment No", default="New", readonly=True, copy=False)

    patient_id = fields.Many2one(
        'hospital.patient',
        string="Patient",
        required=True
    )

    doctor_id = fields.Many2one(
        'hospital.doctor',
        string="Doctor",
        required=True
    )

    appointment_date = fields.Datetime(string="Appointment Date", required=True)
    reason = fields.Text(string="Reason")

    consultation_fee = fields.Float(string="Consultation Fee", related="doctor_id.consultation_fee", readonly=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], default='draft')

    def action_confirm(self):
        for appointment in self:
            appointment.state = 'confirmed'

    def action_done(self):
        for appointment in self:
            appointment.state = 'done'

    def action_cancel(self):
        for appointment in self:
            if appointment.state == 'confirmed':
                raise UserError("Confirmed appointment cannot be cancelled.")
            appointment.state = 'cancel'

    # sequence number vise appointment_number
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('appointment_number','New') == 'New':
                vals['appointment_number'] = self.env['ir.sequence'].next_by_code('hospital.appointment')

        return super().create(vals_list)