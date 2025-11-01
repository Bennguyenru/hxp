# -*- coding: utf-8 -*-
{
    'name': 'HexaPay Unified UI Theme',
    'version': '19.0.1.0.0',
    'category': 'Theme',
    'summary': 'Unified user interface theme for all HexaPay modules',
    'description': '''
        HexaPay Unified UI Theme
        
        Key Features:
        * Consistent menu structure
        * Unified dashboard
        * Custom color scheme
        * Responsive layout
        * Icon standardization
        * Typography consistency
    ''',
    'author': 'HexaPay Team',
    'website': 'https://www.hexapay.com',
    'depends': [
        'web',
        'base',
        'hexapay_core',
    ],
    'data': [
        'views/menu_structure.xml',
        'views/dashboard_views.xml',
        'views/webclient_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'hexapay_ui_theme/static/src/css/hexapay_theme.css',
            'hexapay_ui_theme/static/src/js/hexapay_theme.js',
        ],
        'web.assets_frontend': [
            'hexapay_ui_theme/static/src/css/hexapay_frontend.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
