#!/usr/bin/env bash
# This will be executed on the server
contents=$(cat <<END
server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name anexe.tech www.anexe.tech;
	add_header  X-Served-By  "$HOSTNAME";

	rewrite ^/redirect_me/?$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;

	error_page 404 /notfound.html;
	location = /notfound.html {
		root /usr/share/nginx/html; # Default but just being explicit
		internal;
	}
}

END
)

echo "$contents"
