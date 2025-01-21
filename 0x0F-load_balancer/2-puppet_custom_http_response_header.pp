# 2-puppet_custom_http_response_header.pp

# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Modify the Nginx default configuration to add the custom header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => epp('nginx/default.epp'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Template for Nginx default configuration
file { 'nginx/default.epp':
  ensure  => file,
  content => @(END),
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
            add_header X-Served-By <%= $::hostname %>;
            try_files $uri $uri/ =404;
        }
    }
    | END,
  require => Package['nginx'],
}

# Ensure Nginx is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => Package['nginx'],
  subscribe => File['/etc/nginx/sites-available/default'],
}
