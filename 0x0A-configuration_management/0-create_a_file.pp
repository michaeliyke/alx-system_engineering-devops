# Using Puppet to create a file and ensure it has a specific content

file { '/tmp/school':
	content => 'I love Puppet',
	ensure => file,
	mode => '0744',
	owner => 'www-data',
	group => 'www-data',
}
