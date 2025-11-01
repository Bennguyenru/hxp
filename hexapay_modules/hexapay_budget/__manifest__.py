# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Budget Management',
    'version': '19.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Budget planning and tracking',
    'description': '''
        Budget planning and tracking
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_transaction', 'account'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_budget_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
