{
    'name': 'Real Estate',
    'version': '1.0',
    'summary': 'Real Estate Advertisement',
    'category': 'Sales',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/offers_view.xml',
    ],
    'application': True,
    'installable': True,
}