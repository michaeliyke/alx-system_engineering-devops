# Using Puppet, install flask from pip3 and ensure version 2.1.0, flask installed

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}
