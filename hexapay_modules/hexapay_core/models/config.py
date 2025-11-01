# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class HexaPayConfig(models.Model):
    """Core configuration settings for HexaPay system"""
    _name = 'hexapay.config'
    _description = 'HexaPay Configuration'
    _rec_name = 'company_id'
    
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=True,
        default=lambda self: self.env.company,
        ondelete='cascade'
    )
    
    # API Configuration
    api_enabled = fields.Boolean(
        string='API Enabled',
        default=True
    )
    
    api_key = fields.Char(
        string='API Key',
        help='API key for external integrations'
    )
    
    api_secret = fields.Char(
        string='API Secret',
        help='API secret for authentication'
    )
    
    api_url = fields.Char(
        string='API URL',
        help='Base URL for API endpoints'
    )
    
    # Currency Settings
    default_currency_id = fields.Many2one(
        'res.currency',
        string='Default Currency',
        default=lambda self: self.env.company.currency_id
    )
    
    multi_currency_enabled = fields.Boolean(
        string='Multi-Currency Enabled',
        default=True
    )
    
    # Transaction Settings
    auto_approve_deposits = fields.Boolean(
        string='Auto-Approve Deposits',
        default=False,
        help='Automatically approve deposit transactions'
    )
    
    auto_approve_withdrawals = fields.Boolean(
        string='Auto-Approve Withdrawals',
        default=False,
        help='Automatically approve withdrawal transactions'
    )
    
    min_deposit_amount = fields.Monetary(
        string='Minimum Deposit',
        currency_field='default_currency_id'
    )
    
    max_deposit_amount = fields.Monetary(
        string='Maximum Deposit',
        currency_field='default_currency_id'
    )
    
    min_withdrawal_amount = fields.Monetary(
        string='Minimum Withdrawal',
        currency_field='default_currency_id'
    )
    
    max_withdrawal_amount = fields.Monetary(
        string='Maximum Withdrawal',
        currency_field='default_currency_id'
    )
    
    # Risk Settings
    risk_scoring_enabled = fields.Boolean(
        string='Risk Scoring Enabled',
        default=True
    )
    
    high_risk_threshold = fields.Float(
        string='High Risk Threshold',
        default=70.0,
        help='Threshold for flagging high-risk transactions (0-100)'
    )
    
    auto_flag_high_risk = fields.Boolean(
        string='Auto-Flag High Risk',
        default=True
    )
    
    # KYC Settings
    kyc_required = fields.Boolean(
        string='KYC Required',
        default=True
    )
    
    kyc_threshold = fields.Monetary(
        string='KYC Threshold',
        currency_field='default_currency_id',
        help='Transaction amount requiring KYC verification'
    )
    
    # Notification Settings
    email_notifications = fields.Boolean(
        string='Email Notifications',
        default=True
    )
    
    sms_notifications = fields.Boolean(
        string='SMS Notifications',
        default=False
    )
    
    push_notifications = fields.Boolean(
        string='Push Notifications',
        default=False
    )
    
    # System Settings
    active = fields.Boolean(
        string='Active',
        default=True
    )
    
    @api.model
    def get_config(self):
        """Get configuration for current company"""
        config = self.search([('company_id', '=', self.env.company.id)], limit=1)
        if not config:
            config = self.create({'company_id': self.env.company.id})
        return config
    
    @api.constrains('high_risk_threshold')
    def _check_risk_threshold(self):
        for record in self:
            if not (0 <= record.high_risk_threshold <= 100):
                raise ValidationError(_('Risk threshold must be between 0 and 100'))


class HexaPayCategory(models.Model):
    """Generic category model for various classifications"""
    _name = 'hexapay.category'
    _description = 'HexaPay Category'
    _order = 'sequence, name'
    _parent_store = True
    _parent_name = 'parent_id'
    
    name = fields.Char(
        string='Name',
        required=True,
        translate=True
    )
    
    code = fields.Char(
        string='Code',
        index=True
    )
    
    parent_id = fields.Many2one(
        'hexapay.category',
        string='Parent Category',
        ondelete='cascade'
    )
    
    parent_path = fields.Char(index=True)
    
    child_ids = fields.One2many(
        'hexapay.category',
        'parent_id',
        string='Child Categories'
    )
    
    type = fields.Selection([
        ('player', 'Player'),
        ('game', 'Game'),
        ('bonus', 'Bonus'),
        ('risk', 'Risk'),
        ('other', 'Other'),
    ], string='Type', required=True, default='other')
    
    sequence = fields.Integer(
        string='Sequence',
        default=10
    )
    
    active = fields.Boolean(
        string='Active',
        default=True
    )
    
    description = fields.Text(
        string='Description'
    )
    
    color = fields.Integer(
        string='Color Index'
    )
    
    _sql_constraints = [
        ('code_unique', 'unique(code, type)', 'Code must be unique per type!')
    ]


class HexaPayTag(models.Model):
    """Generic tag model for flexible tagging"""
    _name = 'hexapay.tag'
    _description = 'HexaPay Tag'
    _order = 'name'
    
    name = fields.Char(
        string='Name',
        required=True,
        translate=True
    )
    
    color = fields.Integer(
        string='Color Index'
    )
    
    active = fields.Boolean(
        string='Active',
        default=True
    )
