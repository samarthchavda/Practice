# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'customer Management',
    'summary': 'Manages employee management system',
    'description':'Manages employee management system',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/view.xml',
        ],
    'installable': True,
    'application':True,
}

