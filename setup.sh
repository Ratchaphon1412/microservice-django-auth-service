#!/bin/bash
docker compose -f docker-compose.yml exec app-auth-server bash
poetry run python3 manage.py makemigrations 
poetry run python3 manage.py migrate
exit