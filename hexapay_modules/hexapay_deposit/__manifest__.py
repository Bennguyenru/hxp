# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Deposit Management',
    'version': '19.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Player deposit processing and tracking',
    'description': '''
        Player deposit processing and tracking
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_transaction', 'hexapay_payment'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_deposit_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
