# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Integration Hub',
    'version': '19.0.1.0.0',
    'category': 'Technical',
    'summary': 'Integration hub for third-party services',
    'description': '''
        Integration hub for third-party services
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_core', 'hexapay_api'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_integration_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
