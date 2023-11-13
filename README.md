# Django Authentication Microservice

![Logo](https://raw.githubusercontent.com/CS211-651/project211-hardcodeexecutable/featureUser/docs/image/Group%202.png?token=GHSAT0AAAAAACG72KP2PYCGYRS3XBBLC7DKZKRCCIA)

## Acknowledgements

- JWT Authentication
- Django Rest Framework
- Python OOP
- Django ORM
- Nginx
- Kafka
- Google Cloud Platform
- Docker Compose
- Jenkins

## Roadmap

- Final Week
  - Jwt using Simple JWT Library in Django
  - Create User Service Database
  - Create User Service API
  - Create User Service Docker Compose
  - Create User Service Jenkins Pipeline
  - Verify Email User Service
  - Login , Register , Update User Service
  - CORS Implementation In Production
  - Django Seeder
  - Permission and Groups
  - Kafka Consumer
  - Kafka Producer

## Third-party libraries

[Django-JWT](https://github.com/jazzband/djangorestframework-simplejwt)

[kafka-python](https://github.com/dpkp/kafka-python)

[django-cors-headers](https://github.com/adamchainz/django-cors-headers)

[django-seed](https://github.com/brobin/django-seed)

## Installation Program

## ENV

```bash
EMAIL_HOST_USER= #Email For Send Email
EMAIL_HOST_PASSWORD= #Password Email For Send Email (Google less Secure App)
```

## use docker-compose development

```bash
git clone https://github.com/Ratchaphon1412/microservice-django-auth-service.git

cd microservice-django-auth-service

docker-compose up -d

```

### migrate database

```bash
docker-compose exec -it app-auth-server bash

poetry run python3 manage.py migrate
```

### create superuser

```bash
docker-compose exec -it app-auth-server bash

poetry run python3 manage.py createsuperuser
```

###

### Run Consumer Kafka Django Background

--topic create_user --group auth in this project

```bash
docker-compose exec -it app-auth-server bash

poetry run python3 manage.py CommandConsumer --topic <topic_name>
--group <group_name>
```

## use docker-compose production

```bash
git clone https://github.com/Ratchaphon1412/microservice-django-auth-service.git

cd microservice-django-auth-service

docker-compose -f docker-compose.prod.yml up -d


```

# Architecture

```
.
|-- DjangoAuth (Cors Project Directory For Setting about Django)
    |-- __init__.py
    |-- asgi.py
    |-- settings.py
    |-- urls.py
    |-- wsgi.py
|-- Infrastructure (Directory For Contain Service In project )
    |-- __init__.py
    |-- kafka (Contain Kafka Service)
        |-- __init__.py
        |-- consumer.py (Contain Kafka Consumer)
        |-- producer.py (Contain Kafka Producer)
    |-- event (Contain Event Service Listening for Consumer Kafka)
        |-- interface
            |-- topicinterface.py (Contain Topic Interface)
        |-- listener
            |-- topic.py (Contain Topic Listener)
    |-- management
        |-- commands
            |-- __init__.py
            |-- CommandConsumer.py (Contain Command Consumer Thread)
    |-- service
        |-- factory (Contain Factory Design Pattern Service)
            |-- email.py (Contain Email Service)
            |-- security.py (Contain Security Service)
        |-- interface
            |-- notification.py (Contain Notification Interface)
    |-- __init__.py
|-- Nginx
    |-- django.conf (Nginx Proxy Config File)
|-- templates (Contain Template HTML)
    |-- auth
        |-- email_verification.html (Email Verification Template HTML)
|-- User
    |-- __init__.py
    |-- migrations (Contain Migration File Auto Generate By Django)
    |-- apps.py (Contain App Config)
    |-- models.py (Contain Model That Auto Generate Migration File)
    |-- serializers.py
    |-- tests.py
    |-- urls.py
    |-- views.py
|-- .env.example
|-- .gitignore
|-- dockerfile
|-- docker-compose.prod.yml
|-- docker-compose.yml
|-- manage.py
|-- poetry.lock
|-- pyproject.toml
|-- README.md
|-- Jenkinsfile
|-- setup.sh
```

# Features

## Authentication

- Register
- Login
- Logout
- Verify Email
- Update User
- Delete User
- Change Password
- Change Email
- Get Information User
- Get All User (For Admin)

## Address User

- Create User Address
- Update User Address
- Delete User Address
- Get User Address
- Get User Address By Id

## Infrastructures

- Kafka Consumer Update Token Payment User (For Payment Service)
- Kafka Producer Create Token Payment User (For Payment Service)
