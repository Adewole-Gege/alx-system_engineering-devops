#!/usr/bin/env bash
# Run on: web-01
# Task: 1 - Create holberton_user with only required privileges
# Purpose: Ensure the user has only `REPLICATION CLIENT` privileges

mysql -u root -p <<EOF
-- Drop user if it already exists
DROP USER IF EXISTS 'holberton_user'@'localhost';

-- Create the user with the correct privileges
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

FLUSH PRIVILEGES;
EOF
