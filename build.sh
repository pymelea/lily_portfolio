#!/bin/bash

# Install python 3.10
yum update -y
yum groupinstall "Development Tools" -y
yum erase openssl-devel -y
yum install openssl11 openssl11-devel  libffi-devel bzip2-devel wget -y
wget https://www.sqlite.org/2023/sqlite-autoconf-3410000.tar.gz
tar zxvf sqlite-autoconf-3410000.tar.gz
(cd sqlite-autoconf-3410000 && ./configure && make && make install) 
yum install python3-pip

# Build the project
echo "Building the project..."
pip install -r requirements.txt

cat /etc/os-release

# echo "Make Migration..."
# python manage.py makemigrations --noinput
# python manage.py migrate --noinput

# echo "Collect Static..."
# python manage.py collectstatic --noinput --clear
