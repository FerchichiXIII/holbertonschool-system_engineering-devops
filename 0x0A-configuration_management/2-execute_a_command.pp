#Using Puppet, create a manifest that kills a process named killmenow.
exec {'killmenow':
  command => 'killmenow',
  path => '/usr/bin/bin:usr/local/bin:bin/',
}
