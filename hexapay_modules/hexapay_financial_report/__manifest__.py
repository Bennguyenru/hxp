# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Financial Reporting',
    'version': '19.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Comprehensive financial reports',
    'description': '''
        Comprehensive financial reports
        
        Key Features:
        * Complete CRUD operations
        * Status workflow management
        * Activity tracking
        * Multi-company support
        * Advanced search and filters
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['hexapay_transaction', 'hexapay_accounting'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/hexapay_financial_report_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
