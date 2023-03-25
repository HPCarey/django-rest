release: cd drf_api && python manage.py makemigrations && python manage.py migrate

web: gunicorn drf_api.wsgi
