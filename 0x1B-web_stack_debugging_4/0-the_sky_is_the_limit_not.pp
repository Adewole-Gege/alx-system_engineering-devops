# 0-the_sky_is_the_limit_not.pp
# This Puppet manifest modifies the Nginx configuration to handle higher concurrent requests.

exec { 'increase_nginx_limit':
  command => 'sed -i "s/15/4069/" /etc/default/nginx && sudo service nginx restart',
  unless  => 'grep "4069" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/:/usr/bin/',
}

exec { 'reload_nginx':
  command     => '/usr/sbin/service nginx reload',
  refreshonly => true,
  subscribe   => Exec['increase_nginx_limit'],
  path        => ['/usr/sbin', '/usr/bin', '/bin'],
}