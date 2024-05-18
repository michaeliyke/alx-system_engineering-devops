# Recreating the server setup of task 0 using puppet

$contents=@("END")
server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name anexe.tech www.anexe.tech;
	add_header  X-Served-By  ${facts['networking']['hostname']};

	rewrite ^/redirect_me/?$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;

	location /hbnb_static {
		alias /data/web_static/current;
		index index.html 0-index.html;
	}

	error_page 404 /notfound.html;
	location = /notfound.html {
		root /usr/share/nginx/html; # Default but just being explicit
		internal;
	}
}

END

exec { 'apt-update':
    command => '/usr/bin/apt-get update',
    path    => ['/usr/bin', '/usr/sbin'],
    before  => Package['nginx'], # Ensure apt-update runs before installing nginx
}

package { 'nginx':
    ensure => installed, # same as ensure installed in this case
}

file { [
    '/data',
    '/data/web_static',
    '/data/web_static/releases',
    '/data/web_static/releases/test/',
    '/data/web_static/shared']:
    ensure  => directory,
    mode    => '0744',
    owner   => $facts['identity']['user'],
    group   => $facts['identity']['group'],
    recurse => true,
}

file { '/data/web_static/current':
    ensure  => link,
    target  => '/data/web_static/releases/test/',
    force   => true, # Force recreation if target exists
    owner   => $facts['identity']['user'],
    group   => $facts['identity']['group'],
    require => File['/data/web_static/releases/test/'],
}

file { [
    '/var/www',
    '/var/www/html',
    '/usr/share/nginx',
    '/usr/share/nginx/html',
    '/etc/nginx',
    '/etc/nginx/sites-enabled',]:
    ensure   => directory,
}

file { ['/data/web_static/releases/test/index.html',
    '/var/www/html/index.html']:
    ensure  => file,
    content => "<html> <body> Hello World! </body> </html>\n",
}

file { '/usr/share/nginx/html/notfound.html':
    ensure  => file,
    content => "<html> <body>Ceci n'est pas une page</body> </html>\n",
}

file { '/etc/nginx/sites-enabled/default':
    ensure  => file,
    content => $contents,
    require => Package['nginx'], # Ensure nginx before changing the config
}

service { 'nginx':
    ensure    => running,
    enable    => true, # Start on boot
    require   => Package['nginx'], # Ensure nginx before starting the service
    subscribe => File['/etc/nginx/sites-enabled/default'], # Restart on config change
}
