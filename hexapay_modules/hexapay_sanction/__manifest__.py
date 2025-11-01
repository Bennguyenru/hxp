# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Sanction Screening',
    'version': '19.0.1.0.0',
    'category': 'Compliance',
    'summary': 'Sanction list screening',
    'description': '''
        Sanction list screening
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_kyc'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_sanction_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
