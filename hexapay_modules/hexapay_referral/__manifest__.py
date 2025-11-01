# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Referral Program',
    'version': '19.0.1.0.0',
    'category': 'CRM',
    'summary': 'Player referral and affiliate program',
    'description': '''
        Player referral and affiliate program
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_player'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_referral_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
