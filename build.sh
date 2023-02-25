#!/bin/bash

# Install python 3.10
sudo yum update -y

# Build the project
echo "Building the project..."
pip install -r requirements.txt

cat /etc/os-release

# echo "Make Migration..."
# python manage.py makemigrations --noinput
# python manage.py migrate --noinput

# echo "Collect Static..."
# python manage.py collectstatic --noinput --clear
