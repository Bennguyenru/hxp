# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Base',
    'version': '19.0.1.0.0',
    'category': 'Technical',
    'summary': 'Base utilities and common functions',
    'description': '''
        Base utilities and common functions
        
        Key Features:
        * Feature 1
        * Feature 2
        * Feature 3
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_core'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/menu_views.xml',
        # 'views/model_views.xml',
        # 'reports/report_templates.xml',
        # 'wizards/wizard_views.xml',
    ],
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            # 'hexapay_base/static/src/js/*.js',
            # 'hexapay_base/static/src/css/*.css',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
