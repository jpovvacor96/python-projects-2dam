# -*- coding: utf-8 -*-
{
    'name': "api-products",

    'summary': """
        Módulo que recoge precios de productos ganaderos de una API REST y los muestra en forma de tabla""",

    'description': """
        Módulo que recoge precios de productos ganaderos de una API REST y los muestra en forma de tabla
    """,

    'author': "José Palomino Ochoa",
    'website': "https://github.com/jpovvacor96/python-projects-2dam",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        'views/templates.xml',
        'views/actions.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True
}
