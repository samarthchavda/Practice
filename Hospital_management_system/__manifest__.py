{
    'name': 'Hospital Management System',
    'description': "manage hospital data",
    'version': '1.0',
    'depends':['base'],
    'data': [
        'security/ir.model.access.csv',
        'view/doctor_view.xml',
        'view/patient_view.xml',
        'view/appointment_view.xml',
        'view/data/sequence.xml',
    ],
    'application': True,
    'installable': True,
}