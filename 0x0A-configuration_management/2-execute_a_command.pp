# Using Puppet, create a manifest that kills a process named killmenow.

exec { '/usr/bin/pkill':
    command     => '/usr/bin/pkill -f killmenow',
    refreshonly => true,
    provider    => 'shell',
}
