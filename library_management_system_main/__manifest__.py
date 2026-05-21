{
    "name": "Library Management Systems(new)",
    "description": "Library Management Systems(new)",
    "version": "1.0",
    "depends": ['base','mail'],
    'assets': {
        'web.assets_backend': [
            'library_management_system_main/static/src/js/library_dashboard.js',
            'library_management_system_main/static/src/xml/library_dashboard.xml',
        ],
    },
    "data": [
        "views/books_view.xml",
        "views/author_view.xml",
        "views/sequence.xml",
        "views/member_view.xml",
        "views/purchase_view.xml",
        "security/ir.model.access.csv",
        "views/dashboard_view.xml",
        "views/issue_view.xml",
        "reports/book_purchase_report.xml",
    ],
    "installable": True,
    "application": True,
}