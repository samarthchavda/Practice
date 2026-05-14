{
    'name': 'OWL Practice',
    'version': '1.0',
    'depends': ['web'],
    'data':[
        # "views/counter_action.xml",
        "views/student_dashboard_action.xml",

    ],
    'assets': {
        'web.assets_backend': [
            # "owl_practice/static/src/js/counter.js",
            # "owl_practice/static/src/xml/counter.xml",
            "owl_practice/static/src/xml/student_dashboard.xml",
            "owl_practice/static/src/js/student_dashboard.js",
        ],
    },

    'installable': True,
    'application': True,
}