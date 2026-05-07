{
    'name': 'Real Estate',
    'description': "real real",
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/offers_view.xml',
        'views/estate_property_views.xml',
    ],
    'application': True,
    'installable': True,
}