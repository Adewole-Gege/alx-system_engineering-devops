# 0x12. Web Stack Debugging #2

## Concepts
This project focuses on debugging a web stack to ensure proper configuration and security best practices. You will work with Linux system administration, DevOps principles, scripting, and debugging techniques.

## Requirements
- All scripts should be written in Bash and be executable.
- Scripts should pass Shellcheck without errors.
- Scripts must be compatible with Ubuntu 20.04 LTS.
- The first line of each script must be `#!/usr/bin/env bash`.
- Each script must include a comment explaining its purpose.

## Tasks
### 0. Run software as another user
- Write a Bash script that accepts a username as an argument and runs `whoami` under that user.
- Example:
  ```bash
  ./0-iamsomeoneelse www-data
  ```
  Expected output:
  ```
  www-data
  ```
- **File:** `0-iamsomeoneelse`

### 1. Run Nginx as Nginx
- Ensure that Nginx runs as the `nginx` user instead of `root`.
- Nginx must listen on all active IPs on port `8080`.
- Modify the configuration and restart the service.
- **File:** `1-run_nginx_as_nginx`

### 2. 7 lines or less
- Achieve the same goal as Task 1 using 7 lines or less.
- **Constraints:**
  - No `;`, `&&`, `wget`, or execution of previous scripts.
- **File:** `100-fix_in_7_lines_or_less`

## Repository Structure
```
|-- alx-system_engineering-devops/
    |-- 0x12-web_stack_debugging_2/
        |-- 0-iamsomeoneelse
        |-- 1-run_nginx_as_nginx
        |-- 100-fix_in_7_lines_or_less
        |-- README.md
