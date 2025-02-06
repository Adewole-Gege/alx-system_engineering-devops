#!/usr/bin/env bash
# Run on: web-01
# Purpose: Create a compressed backup of all MySQL databases

DATE=$(date +'%d-%m-%Y')
echo "Creating MySQL dump..."
mysqldump -u root -p --all-databases > backup.sql

echo "Compressing the backup..."
tar -czvf "$DATE.tar.gz" backup.sql
rm backup.sql

echo "Backup completed: $DATE.tar.gz"
