# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, timedelta
import logging

_logger = logging.getLogger(__name__)


class HexaPayPlayer(models.Model):
    """
    Player model extending res.partner for iGaming VIP customer management.
    Implements 360° Contact View from Agile CRM with iGaming specific features.
    """
    _inherit = 'res.partner'
    
    # ==================== BASIC INFO ====================
    
    is_player = fields.Boolean(
        string='Is Player',
        default=False,
        help='Check if this contact is a player'
    )
    
    player_id = fields.Char(
        string='Player ID',
        copy=False,
        index=True,
        help='Unique player ID from iGaming platform'
    )
    
    username = fields.Char(
        string='Username',
        index=True,
        help='Player username in gaming platform'
    )
    
    player_status = fields.Selection([
        ('lead', 'Lead'),
        ('registered', 'Registered'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('dormant', 'Dormant'),
        ('suspended', 'Suspended'),
        ('self_excluded', 'Self-Excluded'),
        ('closed', 'Closed'),
    ], string='Player Status', default='lead', required=True, tracking=True)
    
    registration_date = fields.Datetime(
        string='Registration Date',
        readonly=True,
        copy=False
    )
    
    first_deposit_date = fields.Datetime(
        string='First Deposit Date',
        readonly=True,
        copy=False
    )
    
    last_login_date = fields.Datetime(
        string='Last Login',
        readonly=True
    )
    
    last_activity_date = fields.Datetime(
        string='Last Activity',
        compute='_compute_last_activity_date',
        store=True
    )
    
    # ==================== VIP & SEGMENTATION ====================
    
    vip_level_id = fields.Many2one(
        'hexapay.vip.level',
        string='VIP Level',
        tracking=True,
        ondelete='restrict'
    )
    
    vip_level_name = fields.Char(
        related='vip_level_id.name',
        string='VIP Level Name',
        store=True
    )
    
    assigned_vip_manager_id = fields.Many2one(
        'res.users',
        string='VIP Manager',
        tracking=True,
        domain=[('share', '=', False)]
    )
    
    player_segment = fields.Selection([
        ('new', 'New Player'),
        ('casual', 'Casual'),
        ('regular', 'Regular'),
        ('high_roller', 'High Roller'),
        ('whale', 'Whale'),
        ('at_risk', 'At Risk'),
        ('churned', 'Churned'),
    ], string='Player Segment', compute='_compute_player_segment', store=True)
    
    lead_score = fields.Integer(
        string='Lead Score',
        compute='_compute_lead_score',
        store=True,
        help='Automatic lead scoring based on behavior and value'
    )
    
    # ==================== FINANCIAL METRICS ====================
    
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id
    )
    
    total_deposits = fields.Monetary(
        string='Total Deposits',
        compute='_compute_financial_metrics',
        store=True,
        currency_field='currency_id'
    )
    
    total_withdrawals = fields.Monetary(
        string='Total Withdrawals',
        compute='_compute_financial_metrics',
        store=True,
        currency_field='currency_id'
    )
    
    net_deposits = fields.Monetary(
        string='Net Deposits',
        compute='_compute_financial_metrics',
        store=True,
        currency_field='currency_id',
        help='Total Deposits - Total Withdrawals'
    )
    
    total_bets = fields.Monetary(
        string='Total Bets',
        compute='_compute_financial_metrics',
        store=True,
        currency_field='currency_id'
    )
    
    total_wins = fields.Monetary(
        string='Total Wins',
        compute='_compute_financial_metrics',
        store=True,
        currency_field='currency_id'
    )
    
    ggr = fields.Monetary(
        string='GGR',
        compute='_compute_financial_metrics',
        store=True,
        currency_field='currency_id',
        help='Gross Gaming Revenue (Bets - Wins)'
    )
    
    ltv = fields.Monetary(
        string='LTV',
        compute='_compute_ltv',
        store=True,
        currency_field='currency_id',
        help='Lifetime Value'
    )
    
    avg_deposit_amount = fields.Monetary(
        string='Avg Deposit',
        compute='_compute_financial_metrics',
        store=True,
        currency_field='currency_id'
    )
    
    avg_bet_size = fields.Monetary(
        string='Avg Bet Size',
        compute='_compute_financial_metrics',
        store=True,
        currency_field='currency_id'
    )
    
    # ==================== BEHAVIORAL METRICS ====================
    
    total_sessions = fields.Integer(
        string='Total Sessions',
        compute='_compute_behavioral_metrics',
        store=True
    )
    
    avg_session_duration = fields.Float(
        string='Avg Session (min)',
        compute='_compute_behavioral_metrics',
        store=True
    )
    
    favorite_game = fields.Char(
        string='Favorite Game',
        compute='_compute_behavioral_metrics',
        store=True
    )
    
    bet_frequency = fields.Float(
        string='Bet Frequency (bets/day)',
        compute='_compute_behavioral_metrics',
        store=True
    )
    
    days_since_last_bet = fields.Integer(
        string='Days Since Last Bet',
        compute='_compute_behavioral_metrics',
        store=True
    )
    
    # ==================== KYC & COMPLIANCE ====================
    
    kyc_status = fields.Selection([
        ('not_started', 'Not Started'),
        ('pending', 'Pending'),
        ('in_review', 'In Review'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected'),
        ('expired', 'Expired'),
    ], string='KYC Status', default='not_started', tracking=True)
    
    kyc_verified_date = fields.Datetime(
        string='KYC Verified Date',
        readonly=True
    )
    
    kyc_verified_by_id = fields.Many2one(
        'res.users',
        string='Verified By',
        readonly=True
    )
    
    kyc_document_ids = fields.Many2many(
        'documents.document',
        string='KYC Documents',
        help='ID, Proof of Address, etc.'
    )
    
    kyc_notes = fields.Text(
        string='KYC Notes'
    )
    
    aml_risk_level = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ], string='AML Risk Level', default='low')
    
    pep_status = fields.Boolean(
        string='PEP (Politically Exposed Person)',
        default=False
    )
    
    # ==================== RESPONSIBLE GAMING ====================
    
    deposit_limit_daily = fields.Monetary(
        string='Daily Deposit Limit',
        currency_field='currency_id'
    )
    
    deposit_limit_weekly = fields.Monetary(
        string='Weekly Deposit Limit',
        currency_field='currency_id'
    )
    
    deposit_limit_monthly = fields.Monetary(
        string='Monthly Deposit Limit',
        currency_field='currency_id'
    )
    
    loss_limit_daily = fields.Monetary(
        string='Daily Loss Limit',
        currency_field='currency_id'
    )
    
    loss_limit_weekly = fields.Monetary(
        string='Weekly Loss Limit',
        currency_field='currency_id'
    )
    
    session_time_limit = fields.Integer(
        string='Session Time Limit (minutes)',
        help='Maximum session duration'
    )
    
    self_exclusion_until = fields.Datetime(
        string='Self-Excluded Until'
    )
    
    reality_check_interval = fields.Integer(
        string='Reality Check Interval (minutes)',
        default=60
    )
    
    # ==================== RELATIONSHIPS ====================
    
    transaction_ids = fields.One2many(
        'hexapay.transaction',
        'player_id',
        string='Transactions'
    )
    
    game_session_ids = fields.One2many(
        'hexapay.game.session',
        'player_id',
        string='Game Sessions'
    )
    
    bonus_ids = fields.One2many(
        'hexapay.player.bonus',
        'player_id',
        string='Bonuses'
    )
    
    risk_alert_ids = fields.One2many(
        'hexapay.risk.alert',
        'player_id',
        string='Risk Alerts'
    )
    
    support_ticket_ids = fields.One2many(
        'hexapay.support.ticket',
        'player_id',
        string='Support Tickets'
    )
    
    deal_ids = fields.One2many(
        'crm.lead',
        'partner_id',
        string='Deals/Opportunities',
        domain=[('type', '=', 'opportunity')]
    )
    
    vip_history_ids = fields.One2many(
        'hexapay.vip.history',
        'player_id',
        string='VIP History'
    )
    
    # ==================== COUNTS ====================
    
    transaction_count = fields.Integer(
        compute='_compute_counts',
        string='Transactions'
    )
    
    session_count = fields.Integer(
        compute='_compute_counts',
        string='Sessions'
    )
    
    bonus_count = fields.Integer(
        compute='_compute_counts',
        string='Bonuses'
    )
    
    ticket_count = fields.Integer(
        compute='_compute_counts',
        string='Tickets'
    )
    
    alert_count = fields.Integer(
        compute='_compute_counts',
        string='Alerts'
    )
    
    # ==================== COMPUTED METHODS ====================
    
    @api.depends('transaction_ids', 'transaction_ids.amount', 'transaction_ids.type')
    def _compute_financial_metrics(self):
        """Calculate all financial metrics from transactions"""
        for player in self:
            transactions = player.transaction_ids.filtered(lambda t: t.status == 'completed')
            
            deposits = transactions.filtered(lambda t: t.type == 'deposit')
            withdrawals = transactions.filtered(lambda t: t.type == 'withdrawal')
            bets = transactions.filtered(lambda t: t.type == 'bet')
            wins = transactions.filtered(lambda t: t.type == 'win')
            
            player.total_deposits = sum(deposits.mapped('amount'))
            player.total_withdrawals = sum(withdrawals.mapped('amount'))
            player.net_deposits = player.total_deposits - player.total_withdrawals
            player.total_bets = sum(bets.mapped('amount'))
            player.total_wins = sum(wins.mapped('amount'))
            player.ggr = player.total_bets - player.total_wins
            
            player.avg_deposit_amount = player.total_deposits / len(deposits) if deposits else 0
            player.avg_bet_size = player.total_bets / len(bets) if bets else 0
    
    @api.depends('ggr', 'net_deposits')
    def _compute_ltv(self):
        """Calculate Lifetime Value"""
        for player in self:
            # Simple LTV = GGR (can be enhanced with predictive models)
            player.ltv = player.ggr
    
    @api.depends('game_session_ids')
    def _compute_behavioral_metrics(self):
        """Calculate behavioral metrics from game sessions"""
        for player in self:
            sessions = player.game_session_ids
            
            player.total_sessions = len(sessions)
            
            if sessions:
                total_duration = sum(sessions.mapped('duration'))
                player.avg_session_duration = total_duration / len(sessions) / 60  # Convert to minutes
                
                # Find favorite game
                game_counts = {}
                for session in sessions:
                    game_counts[session.game_name] = game_counts.get(session.game_name, 0) + 1
                if game_counts:
                    player.favorite_game = max(game_counts, key=game_counts.get)
                
                # Calculate bet frequency
                if player.registration_date:
                    days_active = (fields.Datetime.now() - player.registration_date).days or 1
                    bet_count = len(player.transaction_ids.filtered(lambda t: t.type == 'bet'))
                    player.bet_frequency = bet_count / days_active
                
                # Days since last bet
                last_bet = player.transaction_ids.filtered(lambda t: t.type == 'bet').sorted('transaction_date', reverse=True)[:1]
                if last_bet:
                    player.days_since_last_bet = (fields.Datetime.now() - last_bet.transaction_date).days
    
    @api.depends('last_login_date', 'transaction_ids.transaction_date')
    def _compute_last_activity_date(self):
        """Get the most recent activity date"""
        for player in self:
            dates = [player.last_login_date]
            if player.transaction_ids:
                dates.append(max(player.transaction_ids.mapped('transaction_date')))
            dates = [d for d in dates if d]
            player.last_activity_date = max(dates) if dates else False
    
    @api.depends('ltv', 'days_since_last_bet', 'total_deposits', 'player_status')
    def _compute_player_segment(self):
        """Automatically segment players"""
        for player in self:
            if player.player_status in ['lead', 'registered']:
                player.player_segment = 'new'
            elif player.days_since_last_bet > 90:
                player.player_segment = 'churned'
            elif player.days_since_last_bet > 30:
                player.player_segment = 'at_risk'
            elif player.ltv >= 100000:  # Configurable threshold
                player.player_segment = 'whale'
            elif player.ltv >= 50000:
                player.player_segment = 'high_roller'
            elif player.total_sessions >= 50:
                player.player_segment = 'regular'
            else:
                player.player_segment = 'casual'
    
    @api.depends('ltv', 'total_deposits', 'total_sessions', 'kyc_status', 'email')
    def _compute_lead_score(self):
        """Calculate lead score based on multiple factors"""
        for player in self:
            score = 0
            
            # Financial value
            if player.ltv > 10000:
                score += 50
            elif player.ltv > 5000:
                score += 30
            elif player.ltv > 1000:
                score += 10
            
            # Engagement
            if player.total_sessions > 100:
                score += 30
            elif player.total_sessions > 50:
                score += 20
            elif player.total_sessions > 10:
                score += 10
            
            # Deposits
            if player.total_deposits > 10000:
                score += 20
            elif player.total_deposits > 5000:
                score += 10
            
            # KYC verified
            if player.kyc_status == 'verified':
                score += 10
            
            # Has email
            if player.email:
                score += 5
            
            # Recency penalty
            if player.days_since_last_bet > 30:
                score -= 20
            elif player.days_since_last_bet > 7:
                score -= 10
            
            player.lead_score = max(0, min(100, score))  # Clamp between 0-100
    
    def _compute_counts(self):
        """Compute relationship counts"""
        for player in self:
            player.transaction_count = len(player.transaction_ids)
            player.session_count = len(player.game_session_ids)
            player.bonus_count = len(player.bonus_ids)
            player.ticket_count = len(player.support_ticket_ids)
            player.alert_count = len(player.risk_alert_ids.filtered(lambda a: a.status == 'open'))
    
    # ==================== CONSTRAINTS ====================
    
    @api.constrains('player_id')
    def _check_player_id_unique(self):
        """Ensure player_id is unique"""
        for player in self:
            if player.player_id:
                duplicate = self.search([
                    ('player_id', '=', player.player_id),
                    ('id', '!=', player.id)
                ], limit=1)
                if duplicate:
                    raise ValidationError(_('Player ID must be unique!'))
    
    @api.constrains('deposit_limit_daily', 'deposit_limit_weekly', 'deposit_limit_monthly')
    def _check_deposit_limits(self):
        """Validate deposit limit hierarchy"""
        for player in self:
            if player.deposit_limit_daily and player.deposit_limit_weekly:
                if player.deposit_limit_daily * 7 > player.deposit_limit_weekly:
                    raise ValidationError(_('Daily limit * 7 cannot exceed weekly limit'))
            if player.deposit_limit_weekly and player.deposit_limit_monthly:
                if player.deposit_limit_weekly * 4 > player.deposit_limit_monthly:
                    raise ValidationError(_('Weekly limit * 4 cannot exceed monthly limit'))
    
    # ==================== ACTIONS ====================
    
    def action_view_transactions(self):
        """Open player transactions"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Transactions'),
            'res_model': 'hexapay.transaction',
            'view_mode': 'tree,form',
            'domain': [('player_id', '=', self.id)],
            'context': {'default_player_id': self.id}
        }
    
    def action_view_sessions(self):
        """Open game sessions"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Game Sessions'),
            'res_model': 'hexapay.game.session',
            'view_mode': 'tree,form',
            'domain': [('player_id', '=', self.id)],
            'context': {'default_player_id': self.id}
        }
    
    def action_verify_kyc(self):
        """Open KYC verification wizard"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Verify KYC'),
            'res_model': 'hexapay.player.kyc.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_player_id': self.id}
        }
    
    def action_set_limits(self):
        """Open responsible gaming limits wizard"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Set Limits'),
            'res_model': 'hexapay.player.limit.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_player_id': self.id}
        }
    
    def action_suspend_account(self):
        """Suspend player account"""
        self.ensure_one()
        if self.player_status == 'suspended':
            raise UserError(_('Account is already suspended'))
        
        self.write({
            'player_status': 'suspended',
            'active': False
        })
        
        # Log activity
        self.message_post(
            body=_('Account suspended by %s') % self.env.user.name,
            subject=_('Account Suspended')
        )
    
    def action_reactivate_account(self):
        """Reactivate suspended account"""
        self.ensure_one()
        if self.player_status != 'suspended':
            raise UserError(_('Only suspended accounts can be reactivated'))
        
        self.write({
            'player_status': 'active',
            'active': True
        })
        
        self.message_post(
            body=_('Account reactivated by %s') % self.env.user.name,
            subject=_('Account Reactivated')
        )
