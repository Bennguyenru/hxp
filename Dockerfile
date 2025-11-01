FROM ubuntu:22.04

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Set Odoo variables
ENV OE_USER=odoo
ENV OE_HOME=/odoo
ENV OE_VERSION=19.0
ENV OE_PORT=8069

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    git \
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    build-essential \
    libpq-dev \
    libxml2-dev \
    libxslt1-dev \
    libldap2-dev \
    libsasl2-dev \
    libssl-dev \
    libjpeg-dev \
    libpng-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libxcb1-dev \
    libffi-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    liblzma-dev \
    postgresql-client \
    node-less \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Install wkhtmltopdf
RUN wget -q https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.jammy_amd64.deb \
    && apt-get update \
    && apt-get install -y ./wkhtmltox_0.12.6.1-3.jammy_amd64.deb \
    && rm wkhtmltox_0.12.6.1-3.jammy_amd64.deb \
    && rm -rf /var/lib/apt/lists/*

# Create odoo user
RUN useradd -m -d ${OE_HOME} -U -r -s /bin/bash ${OE_USER}

# Clone Odoo 19
RUN git clone --depth 1 --branch ${OE_VERSION} https://github.com/odoo/odoo.git ${OE_HOME}/odoo-server

# Install Python dependencies with compatibility fixes
RUN pip3 install --upgrade pip setuptools wheel cython
# Install compatible versions of problematic packages first
RUN pip3 install --no-cache-dir gevent==22.10.2 greenlet==2.0.2
# Create a temporary requirements file with fixed versions
RUN sed -e 's/gevent==21.8.0.*/gevent==22.10.2/' -e 's/greenlet==1.1.2/greenlet==2.0.2/' ${OE_HOME}/odoo-server/requirements.txt > /tmp/requirements_fixed.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements_fixed.txt

# Create directories
RUN mkdir -p ${OE_HOME}/custom-addons \
    && mkdir -p ${OE_HOME}/.local/share/Odoo \
    && mkdir -p /var/log/odoo \
    && chown -R ${OE_USER}:${OE_USER} ${OE_HOME} \
    && chown -R ${OE_USER}:${OE_USER} /var/log/odoo

# Copy HexaPay modules
COPY --chown=${OE_USER}:${OE_USER} hexapay_modules/ ${OE_HOME}/custom-addons/

# Create Odoo configuration
RUN echo "[options]\n\
    addons_path = ${OE_HOME}/odoo-server/addons,${OE_HOME}/custom-addons\n\
    data_dir = ${OE_HOME}/.local/share/Odoo\n\
    logfile = /var/log/odoo/odoo.log\n\
    log_level = info\n\
    admin_passwd = admin\n\
    db_host = db\n\
    db_port = 5432\n\
    db_user = odoo\n\
    db_password = odoo\n\
    xmlrpc_port = ${OE_PORT}\n\
    workers = 2\n\
    max_cron_threads = 1" > ${OE_HOME}/odoo.conf \
    && chown ${OE_USER}:${OE_USER} ${OE_HOME}/odoo.conf

# Switch to odoo user
USER ${OE_USER}

# Set working directory
WORKDIR ${OE_HOME}

# Expose port
EXPOSE ${OE_PORT}

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:${OE_PORT}/web/health || exit 1

# Start Odoo
CMD ["python3", "odoo-server/odoo-bin", "-c", "odoo.conf"]
