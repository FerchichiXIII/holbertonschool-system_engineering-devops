# find out why Apache is returning a 500 error.
exec { 'fix':
  command => 'bin/sed -i s/phpp/php/g /var/www/html/index.php',
}
