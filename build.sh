#!/bin/bash
set -o errexit  # Exit if any command fails

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply migrations
python manage.py migrate

# Create superuser if environment variable is set
if [[ "$CREATE_SUPERUSER" == "True" ]]; then
    python manage.py createsuperuser --no-input
fi
