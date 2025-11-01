# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Player Reactivation',
    'version': '19.0.1.0.0',
    'category': 'CRM',
    'summary': 'Dormant player reactivation campaigns',
    'description': '''
        Dormant player reactivation campaigns
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_player', 'hexapay_churn'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_reactivation_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
