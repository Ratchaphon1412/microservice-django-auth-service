#!/bin/bash
poetry run python3 manage.py collectstatic --noinput
poetry run python3 manage.py makemigrations 
poetry run python3 manage.py migrate
poetry run gunicorn --bind 0.0.0.0:8024 DjangoAuth.wsgi
poetry run python3 manage.py ConsumerCommand --topic payment_customer --group auth 


