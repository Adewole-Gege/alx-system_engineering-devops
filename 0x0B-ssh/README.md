# 0x0B. SSH

This project focuses on Secure Shell (SSH) and its practical use for secure remote server access and configuration. By completing this project, you will learn about creating and using SSH key pairs, configuring SSH clients, and implementing automated configurations with Puppet.

## Learning Objectives
At the end of this project, you will be able to explain:

- What is a server and where servers usually live.
- What is SSH and its use cases.
- How to create and use an SSH RSA key pair.
- How to connect to a remote host using SSH RSA key authentication.
- The advantage of using `#!/usr/bin/env bash` over `/bin/bash`.

## Project Files

### Bash Scripts

- **`0-use_a_private_key`**:
  Connects to a server using the private key `~/.ssh/id_rsa`.

- **`1-create_ssh_key_pair`**:
  Generates an RSA key pair with a key size of 4096 bits, saving it as `~/.ssh/id_rsa` and protecting it with a passphrase.

### Configuration Files

- **`2-ssh_config`**:
  Configures the SSH client to use the private key `~/.ssh/id_rsa` and disables password authentication.

- **`3-let_me_in`**:
  Contains the public key to be added to the server's `authorized_keys` for authentication.

### Puppet Manifest

- **`100-puppet_ssh_config.pp`**:
  A Puppet manifest to automate the configuration of the SSH client, ensuring it uses the private key `~/.ssh/id_rsa` and disables password authentication.

## Requirements

- All files should end with a new line.
- All Bash scripts must start with `#!/usr/bin/env bash`.
- All Bash scripts must be executable.
- A `README.md` file at the root of the project is mandatory.

## Usage

### 1. Clone the Repository
```bash
git clone https://github.com/alouatiq/alx-system_engineering-devops.git
cd alx-system_engineering-devops/0x0B-ssh
```

### 2. Run the Bash Scripts

- To connect to a server using the private key:
  ```bash
  ./0-use_a_private_key <server_ip>
  ```

- To generate a new SSH key pair:
  ```bash
  ./1-create_ssh_key_pair
  ```

### 3. Configure the SSH Client
- Copy the contents of `2-ssh_config` to `~/.ssh/config` to apply the configuration.

### 4. Add the Public Key to the Server
- Copy the contents of `3-let_me_in` and append it to the server's `~/.ssh/authorized_keys`.

### 5. Apply the Puppet Manifest
- Use Puppet to configure the SSH client:
  ```bash
  sudo puppet apply 100-puppet_ssh_config.pp
  ```
