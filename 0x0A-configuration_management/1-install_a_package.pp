# Using Puppet, install flask from pip3 and ensure version 2.1.0, flask installed

package { 'python3-pip':
    ensure => 'installed',
}

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
    require  => Package['python3-pip'],
}

package { 'werkzeug':
    ensure   => '2.1.1',
    provider => 'pip3',
    require  => Package['python3-pip'],
}
