# -*- coding: utf-8 -*-
{
    'name': 'HexaPay RTP Monitoring',
    'version': '19.0.1.0.0',
    'category': 'Gaming',
    'summary': 'Return to Player monitoring',
    'description': '''
        Return to Player monitoring
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_game', 'hexapay_bet'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_rtp_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
