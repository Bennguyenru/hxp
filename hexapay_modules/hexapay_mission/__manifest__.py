# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Mission',
    'version': '19.0.1.0.0',
    'category': 'Marketing',
    'summary': 'Mission and quest system',
    'description': '''
        Mission and quest system
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_player', 'hexapay_reward'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_mission_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
