# Allow user holberton to login and open files successfully
exec { 'boost-hard-file-limit-for-holberton':
command => "sed -i '/^holberton soft/s/4/48000/' /etc/security/limits.conf",
path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for Holberton user.
exec {'boost-soft-file-limit-for-holberton':
command => 'sed -i "/^holberton hard/s/5/48000/" /etc/security/limits.conf',
path    => '/usr/local/bin/:/bin/'
}
