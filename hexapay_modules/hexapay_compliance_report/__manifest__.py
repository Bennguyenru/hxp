# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Compliance Reporting',
    'version': '19.0.1.0.0',
    'category': 'Compliance',
    'summary': 'Compliance reporting and audit',
    'description': '''
        Compliance reporting and audit
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_risk', 'hexapay_kyc', 'hexapay_aml'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_compliance_report_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
