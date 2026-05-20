{
    "name": "Library Management Systems(new)",
    "description": "Library Management Systems(new)",
    "version": "1.0",
    "depends": ['base','mail'],
    "data": [
        "views/books_view.xml",
        "views/author_view.xml",
        "views/sequence.xml",
        "views/member_view.xml",
        "views/purchase_view.xml",
        "security/ir.model.access.csv",
        "views/dashboard_view.xml",
        "reports/book_purchase_report.xml",
    ],
    "installable": True,
    "application": True,
}