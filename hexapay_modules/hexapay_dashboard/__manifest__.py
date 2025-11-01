# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Dashboard',
    'version': '19.0.1.0.0',
    'category': 'Reporting',
    'summary': 'Executive dashboard and KPI monitoring',
    'description': '''
        Executive dashboard and KPI monitoring
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_core', 'web'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_dashboard_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
