# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class HexaPayTransaction(models.Model):
    """Transaction tracking for all player financial activities"""
    _name = 'hexapay.transaction'
    _description = 'Player Transaction'
    _order = 'transaction_date desc'
    _rec_name = 'transaction_id'
    
    # Basic Info
    transaction_id = fields.Char(
        string='Transaction ID',
        required=True,
        copy=False,
        index=True,
        help='Unique transaction ID from platform'
    )
    
    player_id = fields.Many2one(
        'res.partner',
        string='Player',
        required=True,
        index=True,
        domain=[('is_player', '=', True)],
        ondelete='restrict'
    )
    
    transaction_date = fields.Datetime(
        string='Date',
        required=True,
        default=fields.Datetime.now,
        index=True
    )
    
    type = fields.Selection([
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
        ('bet', 'Bet'),
        ('win', 'Win'),
        ('bonus', 'Bonus'),
        ('cashback', 'Cashback'),
        ('refund', 'Refund'),
        ('adjustment', 'Adjustment'),
        ('fee', 'Fee'),
        ('commission', 'Commission'),
    ], string='Type', required=True, index=True)
    
    status = fields.Selection([
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
        ('reversed', 'Reversed'),
    ], string='Status', required=True, default='pending', tracking=True)
    
    # Amount
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        required=True,
        default=lambda self: self.env.company.currency_id
    )
    
    amount = fields.Monetary(
        string='Amount',
        required=True,
        currency_field='currency_id'
    )
    
    amount_company_currency = fields.Monetary(
        string='Amount (Company Currency)',
        compute='_compute_amount_company_currency',
        store=True,
        currency_field='company_currency_id'
    )
    
    company_currency_id = fields.Many2one(
        'res.currency',
        string='Company Currency',
        default=lambda self: self.env.company.currency_id
    )
    
    # Payment Info (for deposits/withdrawals)
    payment_method = fields.Selection([
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('e_wallet', 'E-Wallet'),
        ('crypto', 'Cryptocurrency'),
        ('prepaid_card', 'Prepaid Card'),
        ('mobile_payment', 'Mobile Payment'),
        ('other', 'Other'),
    ], string='Payment Method')
    
    payment_provider = fields.Char(
        string='Payment Provider',
        help='e.g., Stripe, PayPal, Skrill'
    )
    
    payment_reference = fields.Char(
        string='Payment Reference',
        help='External payment reference/transaction ID'
    )
    
    card_last_4 = fields.Char(
        string='Card Last 4 Digits',
        size=4
    )
    
    # Gaming Info (for bets/wins)
    game_id = fields.Char(
        string='Game ID',
        index=True
    )
    
    game_name = fields.Char(
        string='Game Name'
    )
    
    game_session_id = fields.Many2one(
        'hexapay.game.session',
        string='Game Session',
        ondelete='set null'
    )
    
    bet_id = fields.Char(
        string='Bet ID',
        help='Unique bet identifier'
    )
    
    round_id = fields.Char(
        string='Round ID',
        help='Game round identifier'
    )
    
    # Bonus Info (for bonus transactions)
    bonus_id = fields.Many2one(
        'hexapay.player.bonus',
        string='Related Bonus',
        ondelete='set null'
    )
    
    bonus_campaign_id = fields.Many2one(
        'hexapay.bonus.campaign',
        string='Bonus Campaign',
        ondelete='set null'
    )
    
    # Additional Info
    reference = fields.Char(
        string='Reference',
        help='Internal reference'
    )
    
    description = fields.Text(
        string='Description'
    )
    
    notes = fields.Text(
        string='Internal Notes'
    )
    
    # Processing Info
    processed_date = fields.Datetime(
        string='Processed Date',
        readonly=True
    )
    
    processed_by_id = fields.Many2one(
        'res.users',
        string='Processed By',
        readonly=True
    )
    
    # Accounting Integration
    account_move_id = fields.Many2one(
        'account.move',
        string='Journal Entry',
        readonly=True,
        ondelete='restrict',
        help='Linked accounting entry'
    )
    
    # Risk & Compliance
    risk_score = fields.Float(
        string='Risk Score',
        digits=(5, 2),
        help='Automated risk score (0-100)'
    )
    
    flagged_for_review = fields.Boolean(
        string='Flagged for Review',
        default=False
    )
    
    reviewed_by_id = fields.Many2one(
        'res.users',
        string='Reviewed By'
    )
    
    review_notes = fields.Text(
        string='Review Notes'
    )
    
    # Computed Fields
    @api.depends('amount', 'currency_id', 'company_currency_id')
    def _compute_amount_company_currency(self):
        for transaction in self:
            if transaction.currency_id == transaction.company_currency_id:
                transaction.amount_company_currency = transaction.amount
            else:
                transaction.amount_company_currency = transaction.currency_id._convert(
                    transaction.amount,
                    transaction.company_currency_id,
                    self.env.company,
                    transaction.transaction_date or fields.Date.today()
                )
    
    # Constraints
    @api.constrains('transaction_id')
    def _check_transaction_id_unique(self):
        for transaction in self:
            duplicate = self.search([
                ('transaction_id', '=', transaction.transaction_id),
                ('id', '!=', transaction.id)
            ], limit=1)
            if duplicate:
                raise ValidationError(_('Transaction ID must be unique!'))
    
    @api.constrains('amount')
    def _check_amount_positive(self):
        for transaction in self:
            if transaction.amount <= 0:
                raise ValidationError(_('Amount must be positive!'))
    
    # Actions
    def action_approve(self):
        """Approve pending transaction"""
        self.ensure_one()
        if self.status != 'pending':
            raise UserError(_('Only pending transactions can be approved'))
        
        self.write({
            'status': 'completed',
            'processed_date': fields.Datetime.now(),
            'processed_by_id': self.env.user.id
        })
        
        # Create accounting entry
        if self.type in ['deposit', 'withdrawal']:
            self._create_account_move()
        
        # Update player metrics
        self.player_id._compute_financial_metrics()
        
        self.message_post(
            body=_('Transaction approved by %s') % self.env.user.name,
            subject=_('Transaction Approved')
        )
    
    def action_reject(self):
        """Reject pending transaction"""
        self.ensure_one()
        if self.status != 'pending':
            raise UserError(_('Only pending transactions can be rejected'))
        
        self.write({
            'status': 'cancelled',
            'processed_date': fields.Datetime.now(),
            'processed_by_id': self.env.user.id
        })
        
        self.message_post(
            body=_('Transaction rejected by %s') % self.env.user.name,
            subject=_('Transaction Rejected')
        )
    
    def action_reverse(self):
        """Reverse completed transaction"""
        self.ensure_one()
        if self.status != 'completed':
            raise UserError(_('Only completed transactions can be reversed'))
        
        # Create reversal transaction
        reversal = self.copy({
            'transaction_id': self.transaction_id + '-REV',
            'amount': -self.amount,
            'type': 'adjustment',
            'description': _('Reversal of %s') % self.transaction_id,
            'reference': self.transaction_id,
            'status': 'completed',
        })
        
        self.write({'status': 'reversed'})
        
        # Reverse accounting entry
        if self.account_move_id:
            self.account_move_id.button_cancel()
        
        self.message_post(
            body=_('Transaction reversed by %s. Reversal: %s') % (self.env.user.name, reversal.transaction_id),
            subject=_('Transaction Reversed')
        )
        
        return {
            'type': 'ir.actions.act_window',
            'name': _('Reversal Transaction'),
            'res_model': 'hexapay.transaction',
            'res_id': reversal.id,
            'view_mode': 'form',
            'target': 'current',
        }
    
    def _create_account_move(self):
        """Create accounting journal entry"""
        self.ensure_one()
        
        # This is a simplified version - actual implementation would be more complex
        journal = self.env['account.journal'].search([('type', '=', 'bank')], limit=1)
        if not journal:
            return
        
        move_vals = {
            'journal_id': journal.id,
            'date': self.transaction_date.date(),
            'ref': self.transaction_id,
            'line_ids': [
                # Debit line
                (0, 0, {
                    'name': self.description or self.transaction_id,
                    'account_id': journal.default_account_id.id,
                    'debit': self.amount if self.type == 'deposit' else 0,
                    'credit': self.amount if self.type == 'withdrawal' else 0,
                    'partner_id': self.player_id.id,
                }),
                # Credit line
                (0, 0, {
                    'name': self.description or self.transaction_id,
                    'account_id': self.env.company.account_journal_payment_debit_account_id.id,
                    'debit': self.amount if self.type == 'withdrawal' else 0,
                    'credit': self.amount if self.type == 'deposit' else 0,
                    'partner_id': self.player_id.id,
                }),
            ],
        }
        
        move = self.env['account.move'].create(move_vals)
        move.action_post()
        
        self.account_move_id = move.id
    
    @api.model
    def create(self, vals):
        """Override create to trigger risk checks"""
        transaction = super().create(vals)
        
        # Auto-calculate risk score
        transaction._calculate_risk_score()
        
        # Auto-flag high-risk transactions
        if transaction.risk_score > 70:
            transaction.flagged_for_review = True
            
            # Create risk alert
            self.env['hexapay.risk.alert'].create({
                'player_id': transaction.player_id.id,
                'rule_id': self.env.ref('hexapay_risk.rule_high_risk_transaction').id,
                'severity': 'high',
                'description': _('High-risk transaction detected: %s') % transaction.transaction_id,
                'related_transaction_ids': [(6, 0, [transaction.id])],
            })
        
        return transaction
    
    def _calculate_risk_score(self):
        """Calculate automated risk score"""
        self.ensure_one()
        score = 0
        
        # Large amount
        if self.amount > 10000:
            score += 30
        elif self.amount > 5000:
            score += 15
        
        # First transaction
        if len(self.player_id.transaction_ids) == 1:
            score += 20
        
        # Unverified KYC
        if self.player_id.kyc_status != 'verified':
            score += 25
        
        # Multiple transactions in short time
        recent_transactions = self.search([
            ('player_id', '=', self.player_id.id),
            ('transaction_date', '>=', fields.Datetime.now() - timedelta(hours=1)),
        ])
        if len(recent_transactions) > 5:
            score += 15
        
        # Withdrawal without deposit
        if self.type == 'withdrawal':
            deposits = self.player_id.transaction_ids.filtered(lambda t: t.type == 'deposit' and t.status == 'completed')
            if not deposits:
                score += 40
        
        self.risk_score = min(100, score)
