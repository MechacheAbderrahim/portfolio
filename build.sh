#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py shell -c "from api.models import UserProfile; import subprocess; raise SystemExit(0 if UserProfile.objects.exists() else subprocess.call(['python', 'manage.py', 'loaddata', 'api_data.json']))"