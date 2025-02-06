#!/usr/bin/env bash
# Run on: web-01 & web-02
# Purpose: Install MySQL 5.7 and start MySQL service

echo "Removing old MySQL installations..."
sudo apt-get remove --purge mysql-* mariadb-* -y
sudo apt-get autoremove -y
sudo rm -rf /var/lib/mysql /etc/mysql

echo "Downloading MySQL 5.7 package..."
wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb

echo "Updating packages..."
sudo apt update

echo "Installing MySQL 5.7..."
sudo apt install -y mysql-server-5.7

echo "Starting MySQL service..."
sudo systemctl start mysql
sudo systemctl enable mysql

echo "MySQL installation complete!"
mysql --version
