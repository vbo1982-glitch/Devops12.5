#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive

sudo apt-get update -y
sudo apt-get install -y mysql-server

sudo sed -i "s/^bind-address.*/bind-address = 192.168.56.10/" /etc/mysql/mysql.conf.d/mysqld.cnf
sudo systemctl enable mysql
sudo systemctl restart mysql

DB_NAME="petclinic"
DB_USER="petuser"
DB_PASS="petpass"

sudo mysql -e "CREATE DATABASE IF NOT EXISTS ${DB_NAME};"
sudo mysql -e "CREATE USER IF NOT EXISTS '${DB_USER}'@'192.168.56.11' IDENTIFIED BY '${DB_PASS}';"
sudo mysql -e "GRANT ALL PRIVILEGES ON ${DB_NAME}.* TO '${DB_USER}'@'192.168.56.11';"
sudo mysql -e "FLUSH PRIVILEGES;"

echo "MySQL готовий, база ${DB_NAME} створена, користувач ${DB_USER} створений."

