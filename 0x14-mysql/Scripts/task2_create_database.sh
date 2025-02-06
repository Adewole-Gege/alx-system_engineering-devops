#!/usr/bin/env bash
# Run on: web-01
# Purpose: Create the 'tyrell_corp' database and the 'nexus6' table

echo "Creating database 'tyrell_corp' and table 'nexus6'..."
mysql -u root -p -e "
CREATE DATABASE tyrell_corp;
USE tyrell_corp;
CREATE TABLE nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);
INSERT INTO nexus6 (name) VALUES ('Leon');
SELECT * FROM nexus6;
"
