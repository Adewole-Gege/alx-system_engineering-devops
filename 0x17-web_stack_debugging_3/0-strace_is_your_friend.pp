# This Puppet manifest fixes the WordPress 500 error caused by a .phpp reference in wp-settings.php

Exec { path => ['/bin', '/usr/bin', '/usr/sbin'] }

exec { 'fix-wordpress':
  # Use sed to replace .phpp with .php in wp-settings.php
  command => '/bin/sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php',
  # Only run if the .phpp typo is still present
  onlyif  => 'grep -q "class-wp-locale.phpp" /var/www/html/wp-settings.php',
  # Notify Apache so it can reload if the file changed
  notify  => Service['apache2'],
}

service { 'apache2':
  ensure => running,
  enable => true,
}
