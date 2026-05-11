{
    'name':'student management',
    'description':'Manage Student Data',
    'version':'1.0',
    'depends':['base'],
    'data':[
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/result.xml',
        'views/final_result.xml',
        "views/sports.xml",
    ],
    'installable': True,
    'application':True,
}