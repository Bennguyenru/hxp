# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, timedelta
import logging

_logger = logging.getLogger(__name__)


class HexapaySecurity(models.Model):
    """Main model for hexapay_security"""
    _name = 'hexapay.security'
    _description = 'HexapaySecurity'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'
    
    # Basic Fields
    name = fields.Char(
        string='Name',
        required=True,
        index=True,
        tracking=True
    )
    
    code = fields.Char(
        string='Code',
        copy=False,
        index=True,
        help='Unique identifier'
    )
    
    active = fields.Boolean(
        string='Active',
        default=True
    )
    
    # Status
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', required=True, tracking=True, index=True)
    
    # Company and User
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=True,
        default=lambda self: self.env.company,
        index=True
    )
    
    user_id = fields.Many2one(
        'res.users',
        string='Responsible',
        default=lambda self: self.env.user,
        tracking=True
    )
    
    # Dates
    date = fields.Datetime(
        string='Date',
        required=True,
        default=fields.Datetime.now,
        index=True
    )
    
    # Description
    description = fields.Text(
        string='Description'
    )
    
    notes = fields.Text(
        string='Internal Notes'
    )
    
    # Constraints
    @api.constrains('code')
    def _check_code_unique(self):
        for record in self:
            if record.code:
                duplicate = self.search([
                    ('code', '=', record.code),
                    ('id', '!=', record.id)
                ], limit=1)
                if duplicate:
                    raise ValidationError(_('Code must be unique!'))
    
    # Actions
    def action_confirm(self):
        """Confirm record"""
        self.ensure_one()
        if self.state != 'draft':
            raise UserError(_('Only draft records can be confirmed'))
        self.write({'state': 'confirmed'})
        self.message_post(
            body=_('Confirmed by %s') % self.env.user.name,
            subject=_('Confirmed')
        )
    
    def action_done(self):
        """Mark as done"""
        self.ensure_one()
        if self.state != 'confirmed':
            raise UserError(_('Only confirmed records can be marked as done'))
        self.write({'state': 'done'})
        self.message_post(
            body=_('Completed by %s') % self.env.user.name,
            subject=_('Completed')
        )
    
    def action_cancel(self):
        """Cancel record"""
        self.ensure_one()
        if self.state == 'done':
            raise UserError(_('Cannot cancel completed records'))
        self.write({'state': 'cancelled'})
        self.message_post(
            body=_('Cancelled by %s') % self.env.user.name,
            subject=_('Cancelled')
        )
    
    def action_reset_to_draft(self):
        """Reset to draft"""
        self.write({'state': 'draft'})
        self.message_post(body=_('Reset to draft'))
    
    @api.model
    def create(self, vals):
        """Override create"""
        if not vals.get('code'):
            vals['code'] = self.env['ir.sequence'].next_by_code('hexapay_security') or 'New'
        return super().create(vals)
