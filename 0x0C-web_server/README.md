# README

## Table of Contents
- [Overview](#overview)
- [Tasks](#tasks)
  - [Task 0: Transfer a File to Your Server](#task-0-transfer-a-file-to-your-server)
  - [Task 1: Install Nginx Web Server](#task-1-install-nginx-web-server)
  - [Task 2: Setup a Domain Name](#task-2-setup-a-domain-name)
  - [Task 3: Redirection](#task-3-redirection)
  - [Task 4: Not Found Page 404](#task-4-not-found-page-404)
  - [Task 5: Install Nginx Web Server (w/ Puppet)](#task-5-install-nginx-web-server-w-puppet)

## Overview
This project involves configuring and managing a web server using Bash scripts and Puppet. The tasks include transferring files, installing Nginx, setting up domains, handling redirections, creating custom error pages, and managing configurations with Puppet.

## Tasks

### Task 0: Transfer a File to Your Server
Write a Bash script to transfer a file to a server using `scp`.

#### Requirements:
1. Accepts 4 parameters:
   - The path to the file to be transferred.
   - The IP of the server.
   - The username to connect with.
   - The path to the SSH private key.
2. Displays usage information if less than 4 parameters are passed.
3. Transfers the file to the user’s home directory (`~/`).
4. Disables strict host key checking.

#### Example:
```bash
./0-transfer_file some_file.txt 192.168.0.1 username /path/to/private_key
```

### Task 1: Install Nginx Web Server
Write a Bash script to install and configure Nginx.

#### Requirements:
1. Install Nginx on the server.
2. Ensure Nginx listens on port 80.
3. Serve a page at `/` containing the string `Hello World!`.
4. Do not use `systemctl` to restart Nginx.

#### Example:
```bash
./1-install_nginx_web_server
curl localhost
# Outputs: Hello World!
```

### Task 2: Setup a Domain Name
Set up a `.tech` domain name and configure DNS records to point to the web server.

#### Requirements:
1. Provide the domain name in a plain text file.
2. Configure an A record to point to the server’s IP.
3. Ensure the domain propagates correctly.

#### Example:
```plaintext
example.tech
```

### Task 3: Redirection
Write a Bash script to configure a 301 redirect in Nginx.

#### Requirements:
1. Redirect requests to `/redirect_me` to another URL.
2. Ensure the response is “301 Moved Permanently”.

#### Example:
```bash
./3-redirection
curl -sI http://your_server_ip/redirect_me
# Location: https://www.youtube.com/watch?v=QH2-TGUlwu4
```

### Task 4: Not Found Page 404
Write a Bash script to configure a custom 404 page in Nginx.

#### Requirements:
1. Create a 404 page that returns the string `Ceci n'est pas une page`.
2. Ensure the HTTP response code is `404 Not Found`.

#### Example:
```bash
./4-not_found_page_404
curl http://your_server_ip/nonexistent_page
# Outputs: Ceci n'est pas une page
```

### Task 5: Install Nginx Web Server (w/ Puppet)
Write a Puppet manifest to install and configure Nginx.

#### Requirements:
1. Install Nginx and ensure it listens on port 80.
2. Serve a page containing `Hello World!`.
3. Add a 301 redirect for `/redirect_me`.

#### Files:
- **Manifest File:** `7-puppet_install_nginx_web_server.pp`
- **Template File:** `nginx/default.erb`

#### Example:
```bash
puppet apply 7-puppet_install_nginx_web_server.pp
curl http://your_server_ip
# Outputs: Hello World!
```

---

### Repo
**GitHub repository:** `alx-system_engineering-devops`  
**Directory:** `0x0C-web_server`

- **0-transfer_file**: Bash script for file transfer.
- **1-install_nginx_web_server**: Bash script to install Nginx.
- **2-setup_a_domain_name**: Plain text file with domain name.
- **3-redirection**: Bash script to configure redirection.
- **4-not_found_page_404**: Bash script to set up a 404 page.
- **7-puppet_install_nginx_web_server.pp**: Puppet manifest to configure Nginx.

