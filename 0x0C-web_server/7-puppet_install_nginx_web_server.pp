# Puppet manifest to install and configure Nginx

# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Create a custom index file
file { '/var/www/html/index.nginx-debian.html':
  ensure  => file,
  content => "Hello World!",
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.nginx-debian.html;
    server_name _;
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    error_page 404 /404.html;
    location = /404.html {
        root /var/www/html;
    }
}
",
}

# Restart Nginx
service { 'nginx':
  ensure => running,
  enable => true,
}
