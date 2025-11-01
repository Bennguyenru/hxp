# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Game Configuration',
    'version': '19.0.1.0.0',
    'category': 'Gaming',
    'summary': 'Game configuration and settings',
    'description': '''
        Game configuration and settings
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_game'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_game_config_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
