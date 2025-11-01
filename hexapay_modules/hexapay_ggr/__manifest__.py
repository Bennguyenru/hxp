# -*- coding: utf-8 -*-
{
    'name': 'HexaPay GGR Calculation',
    'version': '19.0.1.0.0',
    'category': 'Gaming',
    'summary': 'Gross Gaming Revenue calculation',
    'description': '''
        Gross Gaming Revenue calculation
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_bet', 'hexapay_win'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_ggr_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
