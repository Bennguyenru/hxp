# -*- coding: utf-8 -*-
{
    'name': 'HexaPay VIP Manager',
    'version': '19.0.1.0.0',
    'category': 'CRM',
    'summary': 'VIP manager assignment and performance tracking',
    'description': '''
        VIP manager assignment and performance tracking
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_vip'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_vip_manager_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
