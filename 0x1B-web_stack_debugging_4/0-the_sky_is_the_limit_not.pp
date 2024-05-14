# Update the ULIMIT of the nginx defualt file from 15 to 4096
# Restart the Nginx service
exec { 'update-nginx-ulimit':
command =>'sed -i "s/15/4096/" /etc/default/nginx',
path    => '/usr/local/bin/:/bin/'
}

exec { 'restart-nginx-service':
command => '/etc/init.d/nginx restart',
path    =>'/etc/init.d/'
}

# ab -n 2000 -c 100 http://localhost/
