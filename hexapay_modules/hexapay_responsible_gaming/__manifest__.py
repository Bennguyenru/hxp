# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Responsible Gaming',
    'version': '19.0.1.0.0',
    'category': 'Compliance',
    'summary': 'Responsible gaming tools and limits',
    'description': '''
        Responsible gaming tools and limits
        
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
        'views/hexapay_responsible_gaming_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
