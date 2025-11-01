# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Bonus Management',
    'version': '19.0.1.0.0',
    'category': 'Marketing',
    'summary': 'Comprehensive bonus management system',
    'description': '''
        Comprehensive bonus management system
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_player', 'hexapay_transaction'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_bonus_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
