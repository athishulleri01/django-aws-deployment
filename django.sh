#!/bin/bash

echo "Create migrations"
python3 manage.py makemigrations --no-input
echo "=========================="

echo "Migrate"
python3 manage.py migrate --no-input
echo "=========================="

echo "Collect static"
python3 manage.py collectstatic --no-input
echo "=========================="

# Start Gunicorn
gunicorn dryz.wsgi:application --bind 0.0.0.0:8000

# echo "start server"
# python3 manage.py runserver 0.0.0.0:8000
# echo "=========================="
