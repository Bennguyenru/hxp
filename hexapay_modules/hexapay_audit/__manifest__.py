# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Audit Trail',
    'version': '19.0.1.0.0',
    'category': 'Technical',
    'summary': 'Comprehensive audit trail and logging',
    'description': '''
        Comprehensive audit trail and logging
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_core'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_audit_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
