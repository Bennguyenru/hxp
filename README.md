# 🐳 HexaPay Odoo 19 - Docker Build Package

## 📦 Package Overview

This package contains everything needed to build and deploy a custom Odoo 19 Docker image with all 73 HexaPay modules pre-installed.

---

## 📁 Package Contents

```
odoo19_docker_build/
├── Dockerfile                  # Custom Odoo 19 image definition
├── docker-compose.yml          # Multi-container orchestration
├── build_and_test.sh          # Automated build & test script
├── BUILD_GUIDE.md             # Comprehensive build documentation
├── README.md                  # This file
└── hexapay_modules/           # All 73 HexaPay modules
    ├── hexapay_core/
    ├── hexapay_base/
    ├── ... (71 more modules)
    └── hexapay_ui_theme/
```

---

## 🚀 Quick Start

### One-Command Build & Test

```bash
./build_and_test.sh
```

This will:
1. ✅ Verify prerequisites
2. ✅ Build Docker image (10-15 minutes)
3. ✅ Start services
4. ✅ Run health checks
5. ✅ Display access information

### Access Odoo

After successful build:

```
URL: http://localhost:8069
Database: hexapay_test
Email: admin@hexapay.com
Password: admin
```

---

## 📋 Prerequisites

- **Docker**: 20.10+
- **Docker Compose**: 2.0+
- **RAM**: 8GB+
- **Disk Space**: 50GB+
- **OS**: Linux, macOS, or Windows with WSL2

---

## 🎯 What You Get

### Custom Odoo 19 Image

- ✅ Ubuntu 22.04 base
- ✅ Odoo 19.0 from official repository
- ✅ All system dependencies
- ✅ wkhtmltopdf for PDF reports
- ✅ 73 HexaPay modules pre-installed
- ✅ Production-ready configuration

### Services

1. **PostgreSQL 15**
   - Optimized for Odoo
   - Health checks enabled
   - Data persistence

2. **Odoo 19**
   - Custom build with HexaPay modules
   - Auto-restart enabled
   - Log persistence
   - Network isolated

### HexaPay Modules (73)

All validated and tested:
- Core & Base (12)
- CRM & Sales (12)
- Accounting & Finance (12)
- Gaming & Operations (12)
- Bonus & Promotion (12)
- Risk & Compliance (12)
- UI Theme (1)

---

## 📚 Documentation

### Included Guides

1. **BUILD_GUIDE.md** (Comprehensive)
   - Detailed build instructions
   - Configuration options
   - Testing procedures
   - Troubleshooting
   - Performance optimization
   - Security considerations

2. **This README** (Quick Reference)
   - Quick start
   - Basic commands
   - Common issues

### External Documentation

- **Main Project**: See `odoo19_72modules/` directory
- **Test Results**: `TEST_RESULTS.md`
- **Deployment**: `DEPLOYMENT_GUIDE.md`
- **UI Theme**: `UI_THEME_GUIDE.md`

---

## 🔧 Basic Commands

### Build & Deploy

```bash
# Automated build
./build_and_test.sh

# Manual build
docker-compose build
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f odoo
```

### Management

```bash
# Stop services
docker-compose down

# Restart services
docker-compose restart

# Access Odoo shell
docker exec -it hexapay_odoo19 bash

# Access database
docker exec -it hexapay_postgres psql -U odoo
```

### Backup & Restore

```bash
# Backup database
docker exec hexapay_postgres pg_dump -U odoo postgres > backup.sql

# Restore database
docker exec -i hexapay_postgres psql -U odoo postgres < backup.sql
```

---

## 🧪 Testing

### Verify Build

```bash
# Check image
docker images | grep hexapay

# Check containers
docker-compose ps

# Test Odoo access
curl -I http://localhost:8069

# Check modules
docker exec hexapay_odoo19 ls /odoo/custom-addons | wc -l
# Should output: 73
```

### Module Installation Test

1. Open: http://localhost:8069
2. Create database: `hexapay_test`
3. Install: `hexapay_core`, `hexapay_base`, `hexapay_security`
4. Install: `hexapay_ui_theme`
5. Navigate to: HexaPay → Dashboard
6. Verify: KPIs, charts, menu structure

---

## 🐛 Common Issues

### Build Fails

```bash
# Clean Docker cache
docker system prune -a

# Rebuild
docker-compose build --no-cache
```

### Services Won't Start

```bash
# Check logs
docker-compose logs

# Remove volumes and restart
docker-compose down -v
docker-compose up -d
```

### Port Conflict

```bash
# Change port in docker-compose.yml
ports:
  - "8070:8069"  # Use 8070 instead
```

### Modules Not Visible

```bash
# Update apps list in Odoo
# Apps → Update Apps List

# Restart Odoo
docker-compose restart odoo
```

---

## 📊 Build Specifications

### Image Details

- **Base**: Ubuntu 22.04
- **Odoo Version**: 19.0
- **Python**: 3.11
- **PostgreSQL**: 15
- **Size**: ~2.5GB (compressed)
- **Build Time**: 10-15 minutes (first build)

### Resource Requirements

**Minimum**:
- CPU: 2 cores
- RAM: 4GB
- Disk: 20GB

**Recommended**:
- CPU: 4 cores
- RAM: 8GB
- Disk: 50GB

**Production**:
- CPU: 8+ cores
- RAM: 16GB+
- Disk: 100GB+

---

## 🔒 Security Notes

### Default Credentials

**⚠️ CHANGE IN PRODUCTION**

- Master Password: `admin`
- Database User: `odoo`
- Database Password: `odoo`
- Admin Email: `admin@hexapay.com`
- Admin Password: `admin`

### Production Checklist

- [ ] Change all default passwords
- [ ] Enable HTTPS
- [ ] Configure firewall
- [ ] Set up backups
- [ ] Enable monitoring
- [ ] Review access controls
- [ ] Configure log rotation

---

## 📈 Performance Tips

### Docker Resources

Increase in Docker Desktop:
- Settings → Resources
- CPU: 4+ cores
- Memory: 8GB+

### Odoo Workers

Edit `odoo.conf` in container:
```ini
workers = 4
max_cron_threads = 2
```

### Database Optimization

```bash
# Vacuum database
docker exec hexapay_postgres psql -U odoo -c "VACUUM ANALYZE;"
```

---

## 🎯 Success Criteria

Build is successful if:

✅ Docker image builds without errors
✅ Containers start and stay running
✅ PostgreSQL health check passes
✅ Odoo accessible at http://localhost:8069
✅ All 73 modules in container
✅ Database creation works
✅ Modules install successfully

---

## 📞 Support

### Troubleshooting Steps

1. **Check logs**: `docker-compose logs`
2. **Verify config**: `docker exec hexapay_odoo19 cat /odoo/odoo.conf`
3. **Test database**: `docker exec hexapay_postgres pg_isready -U odoo`
4. **Review documentation**: `BUILD_GUIDE.md`

### Resources

- **Build Guide**: `BUILD_GUIDE.md` (detailed)
- **Main Documentation**: `../odoo19_72modules/`
- **Odoo Docs**: https://www.odoo.com/documentation/19.0/
- **Docker Docs**: https://docs.docker.com/

---

## 🎉 Next Steps

1. ✅ Run `./build_and_test.sh`
2. ✅ Wait for build completion
3. ✅ Access http://localhost:8069
4. ✅ Create database
5. ✅ Install modules
6. ✅ Explore HexaPay dashboard
7. ✅ Deploy to production

---

## 📦 Package Information

**Version**: 1.0.0
**Date**: 2025-11-01
**Status**: ✅ Production Ready
**Modules**: 73 (all validated)
**Build Time**: 10-15 minutes
**Image Size**: ~2.5GB

---

## 🏆 Features

✅ **Automated Build** - One command deployment
✅ **Pre-configured** - Ready to use
✅ **All Modules** - 73 modules included
✅ **Health Checks** - Automatic monitoring
✅ **Data Persistence** - Volumes configured
✅ **Production Ready** - Optimized settings
✅ **Well Documented** - Comprehensive guides

---

**Ready to build? Run `./build_and_test.sh` and get started! 🚀**

---

**Developed by**: HexaPay Team
**Powered by**: Manus AI
**Version**: 19.0.1.0.0
**License**: LGPL-3

---

**Happy Building! 🐳✨**
