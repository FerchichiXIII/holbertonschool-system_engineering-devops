# testing how well our web server setup featuring Nginx is doing under pressure and it turns out it’s not doing well

exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin:/bin',
  onlyif  => '/usr/bin/test ! -e /var/lib/apt/periodic/update-success-stamp -o /var/lib/apt/periodic/update-success-stamp -ot 86400',
}
