#!/usr/bin/env bash
# Run on: web-01 & web-02
# Purpose: Insert test data on web-01 and verify if it appears on web-02

echo "Inserting test data into primary database..."
mysql -u root -p -e "
USE tyrell_corp;
INSERT INTO nexus6 (name) VALUES ('Roy');
"

echo "Checking if data appears on the replica server..."
mysql -u root -p -e "
USE tyrell_corp;
SELECT * FROM nexus6;
"
