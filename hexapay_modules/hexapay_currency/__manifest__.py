# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Multi-Currency',
    'version': '19.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Advanced multi-currency support',
    'description': '''
        Advanced multi-currency support
        
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
        'views/hexapay_currency_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
