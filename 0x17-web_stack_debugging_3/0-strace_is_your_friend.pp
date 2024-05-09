# This scripts seeks to make changes fixing issues in the php conf file

# Stop Apache service
exec { 'stop_apache2_service':
    command => 'service apache2 stop',
    path    => '/usr/bin',
}

# Ensure the envvars file exists
exec { 'Fix_errors_in_php_conf':
    command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
    path    => '/usr/local/bin/:/bin/',
}

# Restart Apache service
exec { 'restart_apache2_service':
    command => 'service apache2 start',
    path    => '/usr/bin',
}
