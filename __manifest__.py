# -*- coding: utf-8 -*-
{
    'name': "Expenses",

    'summary': """A module for control the cost of the projects""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/cost.xml',
        #'security/security.xml',
        'report.xml',
        'reports.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}