#!/bin/bash
################################################################################
# HexaPay Odoo 19 - Docker Build & Test Script
# Builds custom Odoo 19 image with 73 HexaPay modules and tests installation
################################################################################

set -e

echo "================================================================================"
echo "HEXAPAY ODOO 19 - DOCKER BUILD & TEST"
echo "================================================================================"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Functions
print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

# Check Docker availability
echo "Step 1: Checking Docker availability..."
if ! command -v docker &> /dev/null; then
    print_error "Docker is not installed or not available"
    print_info "Please install Docker first: https://docs.docker.com/get-docker/"
    exit 1
fi
print_success "Docker is available"
echo ""

# Check Docker Compose availability
echo "Step 2: Checking Docker Compose availability..."
if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    print_error "Docker Compose is not installed or not available"
    print_info "Please install Docker Compose first"
    exit 1
fi
print_success "Docker Compose is available"
echo ""

# Verify modules
echo "Step 3: Verifying HexaPay modules..."
MODULE_COUNT=$(ls -d hexapay_modules/hexapay_* 2>/dev/null | wc -l)
if [ "$MODULE_COUNT" -ne 73 ]; then
    print_error "Expected 73 modules, found $MODULE_COUNT"
    exit 1
fi
print_success "All 73 modules present"
echo ""

# Build Docker image
echo "Step 4: Building Docker image..."
print_info "This may take 10-15 minutes on first build..."
if docker-compose build --no-cache; then
    print_success "Docker image built successfully"
else
    print_error "Docker build failed"
    exit 1
fi
echo ""

# Start services
echo "Step 5: Starting services..."
if docker-compose up -d; then
    print_success "Services started"
else
    print_error "Failed to start services"
    exit 1
fi
echo ""

# Wait for services to be ready
echo "Step 6: Waiting for services to be ready..."
print_info "Waiting for PostgreSQL..."
for i in {1..30}; do
    if docker exec hexapay_postgres pg_isready -U odoo &> /dev/null; then
        print_success "PostgreSQL is ready"
        break
    fi
    if [ $i -eq 30 ]; then
        print_error "PostgreSQL failed to start"
        docker-compose logs db
        exit 1
    fi
    sleep 2
done

print_info "Waiting for Odoo..."
for i in {1..60}; do
    if curl -s http://localhost:8069/web/health &> /dev/null; then
        print_success "Odoo is ready"
        break
    fi
    if [ $i -eq 60 ]; then
        print_warning "Odoo health check timeout, but may still be starting..."
        break
    fi
    sleep 3
done
echo ""

# Check Odoo logs
echo "Step 7: Checking Odoo logs..."
print_info "Recent Odoo logs:"
docker-compose logs --tail=20 odoo
echo ""

# Test module availability
echo "Step 8: Testing module availability..."
print_info "Checking if modules are accessible..."
if docker exec hexapay_odoo19 ls /odoo/custom-addons | grep hexapay_core &> /dev/null; then
    print_success "Modules are accessible in container"
else
    print_error "Modules not found in container"
    exit 1
fi
echo ""

# Display service status
echo "Step 9: Service status..."
docker-compose ps
echo ""

# Display access information
echo "================================================================================"
echo "BUILD & TEST COMPLETED"
echo "================================================================================"
echo ""
print_success "All services are running!"
echo ""
echo "Access Information:"
echo "  - Odoo URL: http://localhost:8069"
echo "  - Database: postgres"
echo "  - Username: admin@hexapay.com"
echo "  - Password: admin"
echo ""
echo "Next Steps:"
echo "  1. Open browser: http://localhost:8069"
echo "  2. Create database: hexapay_test"
echo "  3. Install modules: hexapay_core, hexapay_base, hexapay_security"
echo "  4. Install UI theme: hexapay_ui_theme"
echo "  5. Navigate to: HexaPay → Dashboard"
echo ""
echo "Useful Commands:"
echo "  - View logs: docker-compose logs -f odoo"
echo "  - Stop services: docker-compose down"
echo "  - Restart: docker-compose restart"
echo "  - Shell access: docker exec -it hexapay_odoo19 bash"
echo ""
print_info "Happy testing! 🚀"
echo ""
