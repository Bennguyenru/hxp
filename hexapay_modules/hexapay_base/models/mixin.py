# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime, timedelta
import logging

_logger = logging.getLogger(__name__)


class HexaPayStatusMixin(models.AbstractModel):
    """Mixin for standard status workflow"""
    _name = 'hexapay.status.mixin'
    _description = 'Status Workflow Mixin'
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', required=True, tracking=True)
    
    def action_submit(self):
        """Submit for approval"""
        self.write({'state': 'pending'})
        self.message_post(body=_('Submitted for approval'))
    
    def action_approve(self):
        """Approve record"""
        self.write({'state': 'approved'})
        self.message_post(body=_('Approved by %s') % self.env.user.name)
    
    def action_reject(self):
        """Reject record"""
        self.write({'state': 'rejected'})
        self.message_post(body=_('Rejected by %s') % self.env.user.name)
    
    def action_cancel(self):
        """Cancel record"""
        self.write({'state': 'cancelled'})
        self.message_post(body=_('Cancelled by %s') % self.env.user.name)
    
    def action_reset_to_draft(self):
        """Reset to draft"""
        self.write({'state': 'draft'})
        self.message_post(body=_('Reset to draft'))


class HexaPayMetricsMixin(models.AbstractModel):
    """Mixin for common metrics calculation"""
    _name = 'hexapay.metrics.mixin'
    _description = 'Metrics Calculation Mixin'
    
    def _calculate_percentage(self, numerator, denominator):
        """Calculate percentage safely"""
        if denominator == 0:
            return 0.0
        return (numerator / denominator) * 100
    
    def _calculate_average(self, values):
        """Calculate average safely"""
        if not values:
            return 0.0
        return sum(values) / len(values)
    
    def _calculate_growth_rate(self, current, previous):
        """Calculate growth rate"""
        if previous == 0:
            return 0.0 if current == 0 else 100.0
        return ((current - previous) / previous) * 100


class HexaPayDateRangeMixin(models.AbstractModel):
    """Mixin for date range filtering"""
    _name = 'hexapay.daterange.mixin'
    _description = 'Date Range Mixin'
    
    date_from = fields.Date(
        string='Date From'
    )
    
    date_to = fields.Date(
        string='Date To'
    )
    
    @api.onchange('date_from', 'date_to')
    def _onchange_dates(self):
        if self.date_from and self.date_to and self.date_from > self.date_to:
            return {
                'warning': {
                    'title': _('Invalid Date Range'),
                    'message': _('Date From cannot be later than Date To')
                }
            }


class HexaPayHelper(models.AbstractModel):
    """Helper utilities"""
    _name = 'hexapay.helper'
    _description = 'HexaPay Helper Utilities'
    
    @api.model
    def format_currency(self, amount, currency=None):
        """Format amount with currency"""
        if not currency:
            currency = self.env.company.currency_id
        return currency.format(amount)
    
    @api.model
    def get_date_ranges(self, period='month'):
        """Get common date ranges"""
        today = fields.Date.today()
        
        if period == 'today':
            return today, today
        elif period == 'yesterday':
            yesterday = today - timedelta(days=1)
            return yesterday, yesterday
        elif period == 'week':
            start = today - timedelta(days=today.weekday())
            return start, today
        elif period == 'month':
            start = today.replace(day=1)
            return start, today
        elif period == 'quarter':
            quarter = (today.month - 1) // 3
            start = today.replace(month=quarter * 3 + 1, day=1)
            return start, today
        elif period == 'year':
            start = today.replace(month=1, day=1)
            return start, today
        else:
            return today, today
    
    @api.model
    def generate_unique_code(self, prefix='HP', length=8):
        """Generate unique code"""
        import random
        import string
        chars = string.ascii_uppercase + string.digits
        code = prefix + ''.join(random.choices(chars, k=length))
        return code
