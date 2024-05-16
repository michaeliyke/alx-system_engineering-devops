#!/usr/bin/env bash
# Remove  nginx

# Remove nginx
if command -v nginx >& /dev/null; then
	apt-get purge nginx -y >& /dev/null;
	apt-get autoremove -y >& /dev/null
fi

# Remove data directory
if [ -d "/data/" ]; then rm -rvf "/data/"; fi

# Remove nginx settings
if [ -d "/etc/nginx" ]; then rm -rvf "/etc/nginx"; fi
if [ -d "/var/www/" ]; then rm -rvf "/var/www"; fi
if [ -d "/usr/share/nginx" ]; then rm -rvf "/usr/share/nginx"; fi

# Install Nginx
# apt-get update
# apt-get install nginx -y >& /dev/null
# service nginx status
#