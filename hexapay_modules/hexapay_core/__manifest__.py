# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Core',
    'version': '19.0.1.0.0',
    'category': 'Technical',
    'summary': 'Core configuration and base models for HexaPay system',
    'description': '''
        HexaPay Core Module
        
        Key Features:
        * Core configuration management
        * Category and tag system
        * Base models and utilities
        * API configuration
        * System settings
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': ['base', 'mail', 'web'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/menu_views.xml',
        'views/config_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
