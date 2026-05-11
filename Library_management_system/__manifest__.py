{
    'name': 'Library Management System',
    'description': 'Library Management System',
    'version': '1.0',
    'depends': ['base'],
    'data':[
        'security/ir.model.access.csv',
        'views/view.xml',
        'views/author.xml',
        'views/customer.xml',
        'views/issue.xml',
    ],
    'application':True,
    'installable':True,
}