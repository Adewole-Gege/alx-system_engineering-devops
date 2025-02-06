#!/usr/bin/env bash
# Run on: web-01
# Purpose: Create 'replica_user' for MySQL replication

echo "Creating MySQL replication user 'replica_user'..."
mysql -u root -p -e "
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'your_secure_password';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
FLUSH PRIVILEGES;
SELECT user, Repl_slave_priv FROM mysql.user;
"
