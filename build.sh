#!/bin/bash

# Install python 3.10
yum update -y
yum groupinstall "Development Tools" -y
yum erase openssl-devel -y
yum install openssl11 openssl11-devel  libffi-devel bzip2-devel wget -y
wget https://www.python.org/ftp/python/3.10.4/Python-3.10.4.tgz
tar -xf Python-3.10.4.tgz
(cd Python-3.10.4 && ./configure --enable-optimizations && make altinstall) 
yum install python3-pip
python3.10 -m pip install -r requirements.txt

# Build the project
echo "Building the project..."
# pip install -r requirements.txt

cat /etc/os-release

# echo "Make Migration..."
# python manage.py makemigrations --noinput
# python manage.py migrate --noinput

# echo "Collect Static..."
# python manage.py collectstatic --noinput --clear
