# HexaPay Unified UI Theme

## Overview

The **HexaPay Unified UI Theme** provides a consistent, modern, and professional user interface for all 72 HexaPay modules. It includes a comprehensive menu structure, executive dashboard, and unified styling across the entire system.

## Features

### 1. Unified Menu Structure
- **Hierarchical Navigation**: 6 main sections with logical sub-menus
  - Dashboard
  - Players & CRM
  - Transactions & Finance
  - Gaming & Operations
  - Bonus & Promotions
  - Risk & Compliance
  - Reports & Analytics
  - Configuration

### 2. Executive Dashboard
- **Real-time KPIs**:
  - Active Players
  - Total Deposits
  - Total Withdrawals
  - GGR (Gross Gaming Revenue)
  - New Registrations
  - Active Bonuses
  - Pending KYC
  - Risk Alerts

- **Interactive Charts**:
  - Revenue Trend (Line Chart)
  - Player Status Distribution (Doughnut Chart)

- **Data Tables**:
  - Top Players by GGR
  - Recent Transactions

- **System Alerts**:
  - Real-time notifications
  - Priority-based coloring

### 3. Consistent Styling
- **Color Palette**:
  - Primary: #2C3E50 (Dark Blue)
  - Secondary: #3498DB (Blue)
  - Success: #27AE60 (Green)
  - Warning: #F39C12 (Orange)
  - Danger: #E74C3C (Red)
  - Info: #16A085 (Teal)

- **Gradient Backgrounds**:
  - Modern gradient effects on KPI cards
  - Smooth transitions and animations

- **Typography**:
  - Clear hierarchy
  - Readable font sizes
  - Professional appearance

### 4. Responsive Design
- Mobile-friendly layout
- Adaptive grid system
- Touch-optimized controls

### 5. UI Components
- **KPI Cards**: Eye-catching metric displays
- **Charts**: Interactive data visualization
- **Tables**: Clean data presentation
- **Badges**: Status indicators
- **Buttons**: Consistent styling
- **Forms**: Professional layout

## Installation

### Prerequisites
- Odoo 19.0
- hexapay_core module installed

### Steps

1. **Install the module**:
   ```bash
   # Copy to addons directory
   cp -r hexapay_ui_theme /path/to/odoo/addons/
   
   # Restart Odoo
   sudo systemctl restart odoo19
   ```

2. **Activate in Odoo**:
   - Go to Apps
   - Update Apps List
   - Search for "HexaPay Unified UI Theme"
   - Click Install

3. **Access Dashboard**:
   - Navigate to HexaPay → Dashboard
   - Enjoy the unified interface!

## Configuration

### Menu Customization

The menu structure is defined in `views/menu_structure.xml`. You can customize:
- Menu order (sequence)
- Menu labels
- Menu hierarchy
- Menu visibility

### Dashboard Customization

The dashboard can be customized by modifying:
- `views/dashboard_views.xml` - HTML structure
- `static/src/css/hexapay_theme.css` - Styling
- `static/src/js/hexapay_theme.js` - Functionality

### Color Scheme

To change the color scheme, edit the CSS variables in `hexapay_theme.css`:

```css
:root {
    --hexapay-primary: #2C3E50;
    --hexapay-secondary: #3498DB;
    --hexapay-success: #27AE60;
    --hexapay-warning: #F39C12;
    --hexapay-danger: #E74C3C;
    --hexapay-info: #16A085;
}
```

## Menu Structure

```
HexaPay
├── Dashboard
├── Players & CRM
│   ├── Players
│   ├── Leads
│   ├── Opportunities
│   ├── VIP Management
│   │   ├── VIP Levels
│   │   └── VIP Managers
│   ├── Segmentation
│   └── Retention
├── Transactions & Finance
│   ├── Transactions
│   ├── Deposits
│   ├── Withdrawals
│   ├── Payment Processing
│   ├── Accounting
│   ├── Reconciliation
│   └── Financial Reports
├── Gaming & Operations
│   ├── Games
│   ├── Game Sessions
│   ├── Bets
│   ├── Wins
│   ├── Analytics
│   │   ├── GGR Reports
│   │   └── RTP Monitoring
│   ├── Tournaments
│   └── Leaderboards
├── Bonus & Promotions
│   ├── Bonuses
│   ├── Campaigns
│   ├── Bonus Rules
│   ├── Wagering
│   ├── Cashback
│   ├── Free Spins
│   ├── Promo Codes
│   └── Abuse Detection
├── Risk & Compliance
│   ├── KYC Management
│   ├── AML Monitoring
│   ├── Fraud Detection
│   ├── Risk Management
│   │   ├── Risk Alerts
│   │   └── Risk Rules
│   ├── Responsible Gaming
│   │   ├── Self-Exclusion
│   │   └── Limits
│   ├── Screening
│   │   ├── PEP Screening
│   │   └── Sanction Lists
│   └── Compliance Reports
├── Reports & Analytics
│   ├── Executive Dashboard
│   ├── Player Reports
│   ├── Financial Reports
│   ├── Gaming Reports
│   └── Compliance Reports
└── Configuration
    ├── Settings
    ├── Users & Access
    ├── Integrations
    ├── Notifications
    └── Categories & Tags
```

## Dashboard Widgets

### KPI Cards
- **Active Players**: Current active player count
- **Total Deposits**: Sum of all deposits in period
- **Total Withdrawals**: Sum of all withdrawals in period
- **GGR**: Gross Gaming Revenue
- **New Registrations**: New player signups
- **Active Bonuses**: Currently active bonus instances
- **Pending KYC**: KYC verifications awaiting review
- **Risk Alerts**: Active risk alerts requiring attention

### Charts
- **Revenue Trend**: Line chart showing deposits, withdrawals, and GGR over time
- **Player Status**: Doughnut chart showing distribution of player statuses

### Tables
- **Top Players by GGR**: Top 5 players ranked by GGR
- **Recent Transactions**: Latest 5 transactions

### Alerts
- System-wide alerts and notifications
- Color-coded by priority (danger, warning, info)

## Technical Details

### Dependencies
- `web`: Odoo web module
- `base`: Odoo base module
- `hexapay_core`: HexaPay core module

### Assets
- **CSS**: `static/src/css/hexapay_theme.css`
- **JavaScript**: `static/src/js/hexapay_theme.js`
- **External**: Chart.js 3.9.1 (CDN)

### Data Files
- `views/menu_structure.xml`: Menu definitions
- `views/dashboard_views.xml`: Dashboard template
- `views/webclient_templates.xml`: WebClient customizations

## Customization Guide

### Adding New KPI Cards

1. Update `dashboard_views.xml`:
```xml
<div class="col-md-3">
    <div class="hexapay_kpi_card">
        <div class="hexapay_kpi_content">
            <div class="hexapay_kpi_label">Your KPI</div>
            <div class="hexapay_kpi_value" data-metric="your_kpi">0</div>
        </div>
    </div>
</div>
```

2. Update `hexapay_theme.js`:
```javascript
this.state.kpis.your_kpi = 0;
```

### Adding New Charts

1. Add canvas element in `dashboard_views.xml`:
```xml
<canvas id="your_chart_id"></canvas>
```

2. Initialize chart in `hexapay_theme.js`:
```javascript
const ctx = document.getElementById('your_chart_id');
new Chart(ctx, { /* config */ });
```

### Styling Custom Components

Add styles to `hexapay_theme.css`:
```css
.your_custom_class {
    /* Your styles */
}
```

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Performance

- Optimized CSS with minimal selectors
- Lazy-loaded charts
- Efficient data fetching
- Responsive images
- Minimal JavaScript footprint

## Accessibility

- ARIA labels on interactive elements
- Keyboard navigation support
- High contrast mode compatible
- Screen reader friendly

## Support

For issues or questions:
- Check module documentation
- Review Odoo logs
- Contact HexaPay support team

## License

LGPL-3

## Credits

**Developed by**: HexaPay Team
**Version**: 19.0.1.0.0
**Last Updated**: 2025-11-01

---

**Enjoy the unified HexaPay experience!** 🎨
