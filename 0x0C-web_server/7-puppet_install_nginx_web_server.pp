# Setup and nginx web inserver
package { 'nginx':
  ensure => 'installed',
}

$root='/var/www'
$notfound='/usr/share/nginx/html/notfound.html'


file { [
    $root, "${root}/html", '/usr/share', '/usr/share/nginx',
    '/usr/share/nginx/html', '/etc/nginx', '/etc/nginx/sites-enabled',
    '/etc/nginx/sites-available',]:
  ensure  => directory,
}

file { "${root}/html/index.html":
  ensure  => file,
  content => "<html> <body> Hello World! </body> </html>\n",
}

# 404 page
file { $notfound: # To show an example of using a variable
  ensure  => file,
  content => "<html> <body>Ceci n'est pas une page</body> </html>\n",
}

file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  content => generate('/update_nginx_config.sh'),
}

file { '/etc/nginx/sites-available/default':
  ensure => link,
  force  => true,
  target => '/etc/nginx/sites-enabled/default',
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  require   => Package['nginx'],
  subscribe => File['/etc/nginx/sites-enabled/default'],
}
