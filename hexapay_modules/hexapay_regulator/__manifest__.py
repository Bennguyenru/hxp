# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Regulator Reporting',
    'version': '19.0.1.0.0',
    'category': 'Compliance',
    'summary': 'Regulatory reporting and submission',
    'description': '''
        Regulatory reporting and submission
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_compliance_report'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_regulator_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
