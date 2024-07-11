#!/bin/bash

echo "Create migrations"
python3 manage.py makemigrations 
echo "=========================="

echo "Migrate"
python3 manage.py migrate 
echo "=========================="

echo "Collect static"
python3 manage.py collectstatic 
echo "=========================="

# Start Gunicorn
gunicorn -b 0.0.0.0:8000 dryz.wsgi:application --timeout 300

# use only development 
# echo "start server"
# python3 manage.py runserver 0.0.0.0:8000
# echo "=========================="
