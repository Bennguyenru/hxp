# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Self-Exclusion',
    'version': '19.0.1.0.0',
    'category': 'Compliance',
    'summary': 'Self-exclusion management',
    'description': '''
        Self-exclusion management
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_responsible_gaming'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_self_exclusion_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
