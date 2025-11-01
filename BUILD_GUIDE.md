# 🐳 HexaPay Odoo 19 - Docker Build & Test Guide

## 📋 Overview

This guide provides complete instructions for building a custom Odoo 19 Docker image with all 73 HexaPay modules pre-installed and testing the installation.

---

## 🎯 What's Included

### Docker Configuration

1. **Dockerfile**
   - Based on Ubuntu 22.04
   - Odoo 19.0 from official GitHub repository
   - All system dependencies installed
   - wkhtmltopdf for PDF reports
   - 73 HexaPay modules pre-copied
   - Production-ready configuration

2. **docker-compose.yml**
   - PostgreSQL 15 database
   - Custom Odoo 19 build
   - Health checks configured
   - Volume persistence
   - Network isolation
   - Auto-restart enabled

3. **build_and_test.sh**
   - Automated build script
   - Service verification
   - Module availability check
   - Health monitoring
   - User-friendly output

### HexaPay Modules (73)

All validated modules included:
- ✅ Core & Base (12 modules)
- ✅ CRM & Sales (12 modules)
- ✅ Accounting & Finance (12 modules)
- ✅ Gaming & Operations (12 modules)
- ✅ Bonus & Promotion (12 modules)
- ✅ Risk & Compliance (12 modules)
- ✅ UI Theme (1 module)

---

## 🚀 Quick Start

### Prerequisites

```bash
# Required
- Docker 20.10+
- Docker Compose 2.0+
- 8GB+ RAM
- 50GB+ disk space
- Internet connection

# Optional
- Docker Desktop (for GUI management)
```

### Installation Steps

#### Method 1: Automated Build (Recommended)

```bash
# 1. Navigate to build directory
cd odoo19_docker_build

# 2. Run automated build script
./build_and_test.sh

# 3. Wait for completion (10-15 minutes)
# Script will:
# - Verify prerequisites
# - Build Docker image
# - Start services
# - Run health checks
# - Display access information
```

#### Method 2: Manual Build

```bash
# 1. Navigate to build directory
cd odoo19_docker_build

# 2. Build Docker image
docker-compose build --no-cache

# 3. Start services
docker-compose up -d

# 4. Check status
docker-compose ps

# 5. View logs
docker-compose logs -f odoo
```

---

## 📦 Build Process Details

### Stage 1: Base Image Setup

```dockerfile
FROM ubuntu:22.04

# System dependencies installation
# - Python 3.11
# - PostgreSQL client
# - Build tools
# - Image libraries
# - XML/XSLT libraries
```

**Time**: ~3-5 minutes

### Stage 2: Odoo Installation

```dockerfile
# Clone Odoo 19 from GitHub
git clone --depth 1 --branch 19.0 https://github.com/odoo/odoo.git

# Install Python dependencies
pip3 install -r requirements.txt
```

**Time**: ~5-7 minutes

### Stage 3: HexaPay Modules

```dockerfile
# Copy all 73 validated modules
COPY hexapay_modules/ /odoo/custom-addons/
```

**Time**: ~1 minute

### Stage 4: Configuration

```dockerfile
# Create odoo.conf with:
# - Custom addons path
# - Database connection
# - Port configuration
# - Worker settings
```

**Time**: < 1 minute

### Total Build Time

**First build**: 10-15 minutes
**Subsequent builds**: 2-3 minutes (with cache)

---

## 🔧 Configuration

### Dockerfile Configuration

**Key settings**:
```dockerfile
ENV OE_USER=odoo
ENV OE_HOME=/odoo
ENV OE_VERSION=19.0
ENV OE_PORT=8069
```

**Customization**:
- Change `OE_PORT` for different port
- Modify `OE_VERSION` for different Odoo version
- Add custom dependencies in RUN commands

### Docker Compose Configuration

**Database settings**:
```yaml
environment:
  - POSTGRES_DB=postgres
  - POSTGRES_USER=odoo
  - POSTGRES_PASSWORD=odoo
```

**Odoo settings**:
```yaml
ports:
  - "8069:8069"  # Change external port here
volumes:
  - hexapay-web-data:/odoo/.local/share/Odoo
  - hexapay-logs:/var/log/odoo
```

### Odoo Configuration (odoo.conf)

```ini
[options]
addons_path = /odoo/odoo-server/addons,/odoo/custom-addons
data_dir = /odoo/.local/share/Odoo
logfile = /var/log/odoo/odoo.log
log_level = info
admin_passwd = admin
db_host = db
db_port = 5432
db_user = odoo
db_password = odoo
xmlrpc_port = 8069
workers = 2
max_cron_threads = 1
```

**Production recommendations**:
- Change `admin_passwd` to strong password
- Increase `workers` to 4-8 for production
- Set `log_level` to `warn` in production
- Enable `proxy_mode` if behind reverse proxy

---

## 🧪 Testing Procedures

### 1. Build Verification

```bash
# Check if image was built
docker images | grep hexapay

# Expected output:
# odoo19_docker_build_odoo   latest   <image_id>   <size>
```

### 2. Service Health Check

```bash
# Check container status
docker-compose ps

# Expected output:
# NAME                STATUS              PORTS
# hexapay_postgres    Up (healthy)        0.0.0.0:5432->5432/tcp
# hexapay_odoo19      Up                  0.0.0.0:8069->8069/tcp
```

### 3. Database Connection Test

```bash
# Test PostgreSQL connection
docker exec hexapay_postgres pg_isready -U odoo

# Expected output:
# /var/run/postgresql:5432 - accepting connections
```

### 4. Odoo Access Test

```bash
# Test Odoo web interface
curl -I http://localhost:8069

# Expected output:
# HTTP/1.0 303 SEE OTHER
```

### 5. Module Availability Test

```bash
# Check modules in container
docker exec hexapay_odoo19 ls /odoo/custom-addons | grep hexapay | wc -l

# Expected output:
# 73
```

### 6. Log Verification

```bash
# Check Odoo logs
docker-compose logs odoo | tail -50

# Look for:
# - No ERROR messages
# - "HTTP service (werkzeug) running"
# - Module loading messages
```

---

## 🌐 Accessing Odoo

### Initial Setup

1. **Open Browser**:
   ```
   http://localhost:8069
   ```

2. **Create Database**:
   - Master Password: `admin`
   - Database Name: `hexapay_test`
   - Email: `admin@hexapay.com`
   - Password: `admin`
   - Language: English
   - Country: Your country
   - Demo data: No (unchecked)

3. **Wait for Creation**: 2-3 minutes

### Module Installation

#### Phase 1: Core Modules

1. Go to **Apps** menu
2. Click **Update Apps List**
3. Install in order:
   ```
   1. hexapay_core
   2. hexapay_base
   3. hexapay_security
   4. hexapay_api
   ```

#### Phase 2: Functional Modules

Install based on your needs:
- **CRM**: hexapay_player, hexapay_vip, hexapay_lead
- **Finance**: hexapay_transaction, hexapay_payment, hexapay_deposit
- **Gaming**: hexapay_game, hexapay_bet, hexapay_win
- **Bonus**: hexapay_bonus, hexapay_wagering, hexapay_cashback
- **Compliance**: hexapay_kyc, hexapay_aml, hexapay_fraud

#### Phase 3: UI Theme

1. Search for **"HexaPay Unified UI Theme"**
2. Click **Install**
3. Wait for installation
4. Refresh page
5. Navigate to **HexaPay → Dashboard**

---

## 🛠️ Docker Commands

### Basic Operations

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# Restart services
docker-compose restart

# View logs (all services)
docker-compose logs -f

# View logs (Odoo only)
docker-compose logs -f odoo

# View logs (Database only)
docker-compose logs -f db
```

### Container Management

```bash
# Access Odoo container shell
docker exec -it hexapay_odoo19 bash

# Access PostgreSQL shell
docker exec -it hexapay_postgres psql -U odoo

# Check container resource usage
docker stats

# Inspect container
docker inspect hexapay_odoo19
```

### Data Management

```bash
# Backup database
docker exec hexapay_postgres pg_dump -U odoo postgres > backup.sql

# Restore database
docker exec -i hexapay_postgres psql -U odoo postgres < backup.sql

# List volumes
docker volume ls | grep hexapay

# Inspect volume
docker volume inspect hexapay-web-data
```

### Cleanup

```bash
# Stop and remove containers
docker-compose down

# Remove containers and volumes (CAUTION: deletes data)
docker-compose down -v

# Remove images
docker rmi odoo19_docker_build_odoo

# Clean up unused resources
docker system prune -a
```

---

## 🔍 Troubleshooting

### Issue: Build fails with "no space left on device"

**Solution**:
```bash
# Clean up Docker
docker system prune -a --volumes

# Check disk space
df -h
```

### Issue: PostgreSQL won't start

**Solution**:
```bash
# Check logs
docker-compose logs db

# Remove volume and recreate
docker-compose down -v
docker-compose up -d
```

### Issue: Odoo won't start

**Solution**:
```bash
# Check logs
docker-compose logs odoo

# Common issues:
# - Database not ready: Wait 30 seconds
# - Port conflict: Change port in docker-compose.yml
# - Permission issues: Check volume permissions
```

### Issue: Modules not visible

**Solution**:
```bash
# Verify modules in container
docker exec hexapay_odoo19 ls /odoo/custom-addons

# Update apps list in Odoo UI
# Apps → Update Apps List

# Restart Odoo
docker-compose restart odoo
```

### Issue: Cannot access http://localhost:8069

**Solution**:
```bash
# Check if port is in use
netstat -an | grep 8069

# Check container port mapping
docker-compose ps

# Check firewall
sudo ufw status

# Try different port in docker-compose.yml
ports:
  - "8070:8069"
```

### Issue: Slow performance

**Solution**:
```bash
# Increase Docker resources
# Docker Desktop → Settings → Resources
# - CPU: 4+ cores
# - Memory: 8GB+

# Increase Odoo workers
# Edit odoo.conf in container:
docker exec -it hexapay_odoo19 bash
nano /odoo/odoo.conf
# Change: workers = 4
```

---

## 📊 Performance Optimization

### Docker Resources

**Recommended settings**:
```yaml
# In docker-compose.yml
services:
  odoo:
    deploy:
      resources:
        limits:
          cpus: '4'
          memory: 4G
        reservations:
          cpus: '2'
          memory: 2G
```

### Odoo Configuration

**Production settings** (odoo.conf):
```ini
workers = 4
max_cron_threads = 2
limit_memory_hard = 2684354560
limit_memory_soft = 2147483648
limit_request = 8192
limit_time_cpu = 600
limit_time_real = 1200
```

### Database Optimization

```sql
-- Connect to database
docker exec -it hexapay_postgres psql -U odoo

-- Vacuum database
VACUUM ANALYZE;

-- Reindex
REINDEX DATABASE postgres;
```

---

## 🔒 Security Considerations

### Production Checklist

- [ ] Change default admin password
- [ ] Change database password
- [ ] Enable HTTPS (use reverse proxy)
- [ ] Configure firewall rules
- [ ] Disable debug mode
- [ ] Set strong master password
- [ ] Enable database backup
- [ ] Configure log rotation
- [ ] Use secrets management
- [ ] Enable audit logging

### Recommended Setup

```yaml
# Use Docker secrets
secrets:
  db_password:
    file: ./secrets/db_password.txt
  admin_password:
    file: ./secrets/admin_password.txt

services:
  db:
    secrets:
      - db_password
    environment:
      - POSTGRES_PASSWORD_FILE=/run/secrets/db_password
```

---

## 📈 Monitoring

### Health Checks

```bash
# Check Odoo health
curl http://localhost:8069/web/health

# Check database health
docker exec hexapay_postgres pg_isready -U odoo
```

### Log Monitoring

```bash
# Real-time logs
docker-compose logs -f --tail=100

# Error logs only
docker-compose logs | grep ERROR

# Export logs
docker-compose logs > odoo_logs.txt
```

### Resource Monitoring

```bash
# Container stats
docker stats hexapay_odoo19 hexapay_postgres

# Disk usage
docker system df
```

---

## 🎯 Testing Checklist

### Pre-Build
- [ ] Docker installed and running
- [ ] Docker Compose available
- [ ] Sufficient disk space (50GB+)
- [ ] Sufficient RAM (8GB+)
- [ ] All 73 modules present

### Build
- [ ] Image builds successfully
- [ ] No build errors
- [ ] Modules copied to container
- [ ] Configuration created

### Deployment
- [ ] Containers start successfully
- [ ] PostgreSQL healthy
- [ ] Odoo accessible
- [ ] No critical errors in logs

### Functionality
- [ ] Database creation works
- [ ] Core modules install
- [ ] UI theme installs
- [ ] Dashboard accessible
- [ ] Can create records
- [ ] Reports generate

---

## 📞 Support

### Getting Help

1. **Check Logs**:
   ```bash
   docker-compose logs
   ```

2. **Verify Configuration**:
   ```bash
   docker exec hexapay_odoo19 cat /odoo/odoo.conf
   ```

3. **Test Database**:
   ```bash
   docker exec hexapay_postgres psql -U odoo -c "SELECT version();"
   ```

4. **Community Resources**:
   - Odoo Documentation: https://www.odoo.com/documentation/19.0/
   - Docker Documentation: https://docs.docker.com/
   - GitHub Issues: Check repository

---

## 🎉 Success Criteria

Your build is successful if:

✅ Docker image builds without errors
✅ Both containers start and stay running
✅ PostgreSQL health check passes
✅ Odoo web interface accessible
✅ All 73 modules visible in container
✅ Database creation works
✅ Modules install successfully
✅ No critical errors in logs

---

**Build Guide Version**: 1.0.0
**Last Updated**: 2025-11-01
**Status**: ✅ **PRODUCTION READY**

---

**Happy Building! 🚀🐳**
