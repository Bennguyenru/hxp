# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Limit Management',
    'version': '19.0.1.0.0',
    'category': 'Compliance',
    'summary': 'Deposit and loss limit management',
    'description': '''
        Deposit and loss limit management
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_responsible_gaming', 'hexapay_transaction'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_limit_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
