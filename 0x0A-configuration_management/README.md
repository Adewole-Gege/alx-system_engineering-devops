# Configuration Management with Puppet

This project focuses on using **Puppet**, a configuration management tool, to automate system administration tasks. The tasks involve creating files, installing packages, and executing commands on an Ubuntu 20.04 LTS environment.

## Requirements

- All files must be interpreted on Ubuntu 20.04 LTS.
- Each file must:
  - End with a new line.
  - Be named with the `.pp` extension.
  - Start with a comment explaining its purpose.
- Puppet manifests must:
  - Pass `puppet-lint` version 2.1.1 without errors.
  - Run without errors.

## Installation

### Install Puppet
```bash
apt-get install -y ruby=1:2.7+1 --allow-downgrades
apt-get install -y ruby-augeas
apt-get install -y ruby-shadow
apt-get install -y puppet
```

### Install Puppet Lint
```bash
gem install puppet-lint
```

## Tasks

### 0. Create a File
**Objective:** Create a file at `/tmp/school` with specific attributes.

**Requirements:**
- Path: `/tmp/school`
- Permissions: `0744`
- Owner: `www-data`
- Group: `www-data`
- Content: `I love Puppet`

**Manifest File:** `0-create_a_file.pp`

### 1. Install a Package
**Objective:** Install Flask version `2.1.0` using `pip3`.

**Requirements:**
- Package: `Flask`
- Version: `2.1.0`

**Manifest File:** `1-install_a_package.pp`

### 2. Execute a Command
**Objective:** Use Puppet to kill a process named `killmenow`.

**Requirements:**
- Use the `exec` Puppet resource.
- Command: `pkill -f killmenow`

**Manifest File:** `2-execute_a_command.pp`

## Usage

### Validate Puppet Manifests
```bash
puppet-lint <filename>.pp
```

### Apply Puppet Manifests
```bash
puppet apply <filename>.pp
```

### Examples
#### Task 0
```bash
puppet apply 0-create_a_file.pp
ls -l /tmp/school
cat /tmp/school
```

#### Task 1
```bash
puppet apply 1-install_a_package.pp
flask --version
```

#### Task 2
Start the process in one terminal:
```bash
./killmenow
```
Run the manifest in another terminal:
```bash
puppet apply 2-execute_a_command.pp
```
Verify the process is terminated:
```bash
pgrep -f killmenow
```

## Repository Structure
```
alx-system_engineering-devops/
└── 0x0A-configuration_management/
    ├── 0-create_a_file.pp
    ├── 1-install_a_package.pp
    ├── 2-execute_a_command.pp
    └── README.md
```

## Resources
- [Intro to Configuration Management](https://puppet.com/docs/puppet/latest/puppet_index.html)
- [Puppet Resource Type: File](https://puppet.com/docs/puppet/latest/types/file.html)
- [Puppet’s Declarative Language](https://puppet.com/docs/puppet/latest/lang_summary.html)
- [Puppet Lint](http://puppet-lint.com/)
