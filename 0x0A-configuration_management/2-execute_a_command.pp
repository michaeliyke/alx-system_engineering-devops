# Using Puppet, create a manifest that kills a process named killmenow.

exec { 'pkill':
    command     => '/usr/bin/pkill killmenow',
    refreshonly => true,
    provider    => 'shell',
}
