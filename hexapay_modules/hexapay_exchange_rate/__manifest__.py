# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Exchange Rate',
    'version': '19.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Real-time exchange rate management',
    'description': '''
        Real-time exchange rate management
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_currency'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_exchange_rate_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
