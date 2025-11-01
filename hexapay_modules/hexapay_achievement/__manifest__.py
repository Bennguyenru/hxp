# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Achievement',
    'version': '19.0.1.0.0',
    'category': 'Marketing',
    'summary': 'Achievement and badge system',
    'description': '''
        Achievement and badge system
        
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
        'views/hexapay_achievement_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
