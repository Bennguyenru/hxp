/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, onWillStart, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

/**
 * HexaPay Dashboard Component
 */
class HexaPayDashboard extends Component {
    setup() {
        this.orm = useService("orm");
        this.action = useService("action");
        
        this.state = useState({
            period: 'month',
            kpis: {
                active_players: 0,
                total_deposits: 0,
                total_withdrawals: 0,
                ggr: 0,
                new_registrations: 0,
                active_bonuses: 0,
                pending_kyc: 0,
                risk_alerts: 0,
            },
            topPlayers: [],
            recentTransactions: [],
            alerts: [],
            loading: true,
        });
        
        onWillStart(async () => {
            await this.loadDashboardData();
        });
    }
    
    /**
     * Load all dashboard data
     */
    async loadDashboardData() {
        this.state.loading = true;
        
        try {
            // Load KPIs
            await this.loadKPIs();
            
            // Load top players
            await this.loadTopPlayers();
            
            // Load recent transactions
            await this.loadRecentTransactions();
            
            // Load alerts
            await this.loadAlerts();
            
            // Initialize charts
            this.initializeCharts();
            
        } catch (error) {
            console.error('Error loading dashboard data:', error);
        } finally {
            this.state.loading = false;
        }
    }
    
    /**
     * Load KPI metrics
     */
    async loadKPIs() {
        try {
            const result = await this.orm.call(
                'hexapay.dashboard',
                'get_kpi_data',
                [this.state.period]
            );
            
            if (result) {
                Object.assign(this.state.kpis, result);
            }
        } catch (error) {
            console.error('Error loading KPIs:', error);
            // Use mock data for demonstration
            this.state.kpis = {
                active_players: 1247,
                total_deposits: 125430.50,
                total_withdrawals: 87650.25,
                ggr: 37780.25,
                new_registrations: 89,
                active_bonuses: 234,
                pending_kyc: 12,
                risk_alerts: 3,
            };
        }
    }
    
    /**
     * Load top players by GGR
     */
    async loadTopPlayers() {
        try {
            const players = await this.orm.searchRead(
                'res.partner',
                [['is_player', '=', true]],
                ['name', 'vip_level_id', 'ggr', 'player_status'],
                { limit: 5, order: 'ggr desc' }
            );
            
            this.state.topPlayers = players;
        } catch (error) {
            console.error('Error loading top players:', error);
            // Mock data
            this.state.topPlayers = [
                { name: 'Player A', vip_level_id: ['VIP Gold'], ggr: 15420.50, player_status: 'active' },
                { name: 'Player B', vip_level_id: ['VIP Silver'], ggr: 12350.25, player_status: 'active' },
                { name: 'Player C', vip_level_id: ['VIP Gold'], ggr: 10890.75, player_status: 'active' },
                { name: 'Player D', vip_level_id: ['VIP Bronze'], ggr: 9560.00, player_status: 'active' },
                { name: 'Player E', vip_level_id: ['VIP Silver'], ggr: 8720.50, player_status: 'active' },
            ];
        }
    }
    
    /**
     * Load recent transactions
     */
    async loadRecentTransactions() {
        try {
            const transactions = await this.orm.searchRead(
                'hexapay.transaction',
                [],
                ['transaction_id', 'player_id', 'type', 'amount', 'state'],
                { limit: 5, order: 'transaction_date desc' }
            );
            
            this.state.recentTransactions = transactions;
        } catch (error) {
            console.error('Error loading transactions:', error);
            // Mock data
            this.state.recentTransactions = [
                { transaction_id: 'TXN001', player_id: ['Player A'], type: 'deposit', amount: 500.00, state: 'completed' },
                { transaction_id: 'TXN002', player_id: ['Player B'], type: 'withdrawal', amount: 250.00, state: 'processing' },
                { transaction_id: 'TXN003', player_id: ['Player C'], type: 'deposit', amount: 1000.00, state: 'completed' },
                { transaction_id: 'TXN004', player_id: ['Player D'], type: 'bet', amount: 50.00, state: 'completed' },
                { transaction_id: 'TXN005', player_id: ['Player E'], type: 'win', amount: 150.00, state: 'completed' },
            ];
        }
    }
    
    /**
     * Load system alerts
     */
    async loadAlerts() {
        try {
            const alerts = await this.orm.call(
                'hexapay.dashboard',
                'get_system_alerts',
                []
            );
            
            this.state.alerts = alerts || [];
        } catch (error) {
            console.error('Error loading alerts:', error);
            // Mock alerts
            this.state.alerts = [
                { type: 'danger', message: '3 high-risk transactions require review' },
                { type: 'warning', message: '12 KYC verifications pending' },
                { type: 'info', message: 'System maintenance scheduled for tonight 2:00 AM' },
            ];
        }
    }
    
    /**
     * Initialize charts using Chart.js
     */
    initializeCharts() {
        // Revenue trend chart
        const revenueCtx = document.getElementById('hexapay_revenue_chart');
        if (revenueCtx && window.Chart) {
            new Chart(revenueCtx, {
                type: 'line',
                data: {
                    labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
                    datasets: [
                        {
                            label: 'Deposits',
                            data: [25000, 28000, 32000, 35000],
                            borderColor: '#27AE60',
                            backgroundColor: 'rgba(39, 174, 96, 0.1)',
                            tension: 0.4,
                        },
                        {
                            label: 'Withdrawals',
                            data: [18000, 19500, 22000, 24000],
                            borderColor: '#F39C12',
                            backgroundColor: 'rgba(243, 156, 18, 0.1)',
                            tension: 0.4,
                        },
                        {
                            label: 'GGR',
                            data: [7000, 8500, 10000, 11000],
                            borderColor: '#16A085',
                            backgroundColor: 'rgba(22, 160, 133, 0.1)',
                            tension: 0.4,
                        },
                    ],
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: false,
                        },
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                        },
                    },
                },
            });
        }
        
        // Player status pie chart
        const playerStatusCtx = document.getElementById('hexapay_player_status_chart');
        if (playerStatusCtx && window.Chart) {
            new Chart(playerStatusCtx, {
                type: 'doughnut',
                data: {
                    labels: ['Active', 'Inactive', 'Suspended', 'Blocked'],
                    datasets: [{
                        data: [1247, 345, 23, 8],
                        backgroundColor: [
                            '#27AE60',
                            '#95A5A6',
                            '#F39C12',
                            '#E74C3C',
                        ],
                    }],
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'bottom',
                        },
                    },
                },
            });
        }
    }
    
    /**
     * Handle period change
     */
    async onPeriodChange(event) {
        this.state.period = event.target.value;
        await this.loadDashboardData();
    }
    
    /**
     * Format currency
     */
    formatCurrency(value) {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
        }).format(value);
    }
    
    /**
     * Get status badge class
     */
    getStatusBadgeClass(status) {
        const statusMap = {
            'active': 'hexapay_badge_success',
            'completed': 'hexapay_badge_success',
            'processing': 'hexapay_badge_warning',
            'pending': 'hexapay_badge_warning',
            'inactive': 'hexapay_badge_info',
            'suspended': 'hexapay_badge_danger',
            'blocked': 'hexapay_badge_danger',
            'failed': 'hexapay_badge_danger',
        };
        
        return statusMap[status] || 'hexapay_badge_info';
    }
}

HexaPayDashboard.template = "hexapay_ui_theme.hexapay_dashboard_template";

// Register the dashboard
registry.category("actions").add("hexapay_dashboard", HexaPayDashboard);

/**
 * Utility functions for HexaPay theme
 */
export const HexaPayTheme = {
    /**
     * Format number with thousand separators
     */
    formatNumber(num) {
        return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },
    
    /**
     * Format currency
     */
    formatCurrency(amount, currency = 'USD') {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: currency,
        }).format(amount);
    },
    
    /**
     * Get status color
     */
    getStatusColor(status) {
        const colorMap = {
            'active': '#27AE60',
            'completed': '#27AE60',
            'processing': '#F39C12',
            'pending': '#F39C12',
            'inactive': '#95A5A6',
            'suspended': '#E74C3C',
            'blocked': '#E74C3C',
            'failed': '#E74C3C',
        };
        
        return colorMap[status] || '#95A5A6';
    },
    
    /**
     * Show notification
     */
    showNotification(title, message, type = 'info') {
        // Implementation depends on Odoo notification service
        console.log(`[${type}] ${title}: ${message}`);
    },
};

export default HexaPayDashboard;
