# 0x0F. Load Balancer

## Overview
This project focuses on setting up a **load balancer** to manage traffic distribution between multiple web servers. The goal is to improve the redundancy, scalability, and reliability of the web stack. By implementing a load balancer and configuring web servers, we can ensure efficient traffic management and high availability of services.

## Requirements
- All scripts must be written in Bash.
- Scripts must configure brand new Ubuntu 16.04 LTS servers to meet the task requirements.
- Custom HTTP headers must be added to track server responses.
- All scripts should be executable and pass Shellcheck without errors.

## Project Tasks

### 0. Double the Number of Web Servers
- Configure **web-02** to be identical to **web-01**.
- Add a custom HTTP response header `X-Served-By` on both servers, displaying the hostname of the responding server.
- Write a Bash script `0-custom_http_response_header` to automate this setup.

**Key Commands:**
- Install Nginx:
  ```bash
  sudo apt-get update -y && sudo apt-get install -y nginx
  ```
- Add custom header in `/etc/nginx/sites-available/default`:
  ```nginx
  add_header X-Served-By $hostname;
  ```
- Restart Nginx:
  ```bash
  sudo service nginx restart
  ```

---

### 1. Install Your Load Balancer
- Install and configure **HAProxy** on **lb-01**.
- Configure the load balancer to distribute traffic between **web-01** and **web-02** using the round-robin algorithm.
- Write a Bash script `1-install_load_balancer` to automate the setup.

**HAProxy Configuration:**
```haproxy
frontend http_front
    bind *:80
    default_backend http_back

backend http_back
    balance roundrobin
    server web01 54.144.138.231:80 check
    server web02 34.201.61.21:80 check
```

**Key Commands:**
- Install HAProxy:
  ```bash
  sudo apt-get update -y && sudo apt-get install -y haproxy
  ```
- Restart HAProxy:
  ```bash
  sudo service haproxy restart
  ```
- Test Load Balancer:
  ```bash
  curl -sI http://<lb-01-ip>
  ```

---

### 2. Add a Custom HTTP Header with Puppet
- Automate the addition of the `X-Served-By` header using Puppet.
- Write a Puppet manifest `2-puppet_custom_http_response_header.pp` to configure Nginx.

**Example Puppet Manifest:**
```puppet
class nginx_custom_header {
    package { 'nginx':
        ensure => installed,
    }

    file { '/etc/nginx/sites-available/default':
        ensure  => file,
        content => template('nginx/default.erb'),
        notify  => Service['nginx'],
    }

    service { 'nginx':
        ensure     => running,
        enable     => true,
        hasrestart => true,
    }

    exec { 'add_custom_header':
        command => '/bin/sed -i "/server_name _;/a \tadd_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
        notify  => Service['nginx'],
        unless  => '/bin/grep -q "add_header X-Served-By" /etc/nginx/sites-available/default',
    }
}

include nginx_custom_header
```

**Key Commands:**
- Apply Puppet Manifest:
  ```bash
  sudo puppet apply 2-puppet_custom_http_response_header.pp
  ```

---

## Files

| File Name                              | Description                                              |
|---------------------------------------|----------------------------------------------------------|
| `0-custom_http_response_header`       | Bash script to configure Nginx and add a custom header. |
| `1-install_load_balancer`             | Bash script to install and configure HAProxy.           |
| `2-puppet_custom_http_response_header.pp` | Puppet manifest to automate custom header configuration. |

---

## Testing and Validation

- Verify the custom HTTP header:
  ```bash
  curl -sI http://<server-ip> | grep X-Served-By
  ```
- Test HAProxy load balancing:
  ```bash
  curl -sI http://<lb-01-ip> | grep X-Served-By
  ```

---

## Resources
- [Introduction to Load Balancing and HAProxy](https://www.haproxy.org/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Puppet Documentation](https://puppet.com/docs/puppet/)

---

## Author
- **Adewole Gege**

