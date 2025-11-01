# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Free Spin',
    'version': '19.0.1.0.0',
    'category': 'Marketing',
    'summary': 'Free spin management',
    'description': '''
        Free spin management
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_bonus', 'hexapay_game'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_free_spin_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
