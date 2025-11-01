# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Wagering',
    'version': '19.0.1.0.0',
    'category': 'Marketing',
    'summary': 'Wagering requirement tracking',
    'description': '''
        Wagering requirement tracking
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_bonus', 'hexapay_bet'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_wagering_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
