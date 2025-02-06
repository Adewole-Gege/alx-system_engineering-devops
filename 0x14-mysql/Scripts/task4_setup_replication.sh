#!/usr/bin/env bash
# Run on: web-02
# Purpose: Configure MySQL replication (slave) using 'replica_user'

echo "Stopping MySQL slave..."
mysql -u root -p -e "STOP SLAVE;"

echo "Getting master status from web-01..."
read -p "Enter MASTER_LOG_FILE (from web-01): " LOG_FILE
read -p "Enter MASTER_LOG_POS (from web-01): " LOG_POS

echo "Setting up replication..."
mysql -u root -p -e "
CHANGE MASTER TO
MASTER_HOST='web-01-ip',
MASTER_USER='replica_user',
MASTER_PASSWORD='your_secure_password',
MASTER_LOG_FILE='$LOG_FILE',
MASTER_LOG_POS=$LOG_POS;
START SLAVE;
SHOW SLAVE STATUS\G;
"
