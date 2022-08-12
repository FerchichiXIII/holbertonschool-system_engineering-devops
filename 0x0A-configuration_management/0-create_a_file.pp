# create a file in /tmp.
file { '/tmp/scool':
  ensure  => present,
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}
