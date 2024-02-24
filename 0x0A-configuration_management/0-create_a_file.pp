# Using Puppet to create a file and ensure it has a specific content

file { '/tmp/school':
    ensure  => file,
    content => 'I love Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
}
