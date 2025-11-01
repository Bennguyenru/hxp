# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Transaction Management',
    'version': '19.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Comprehensive transaction tracking and management',
    'description': '''
        Comprehensive transaction tracking and management
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_player', 'account'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_transaction_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
