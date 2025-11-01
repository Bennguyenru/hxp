# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Bonus Campaign',
    'version': '19.0.1.0.0',
    'category': 'Marketing',
    'summary': 'Bonus campaign management',
    'description': '''
        Bonus campaign management
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_bonus'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_bonus_campaign_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
