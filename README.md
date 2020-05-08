# Clowning Around

This is an assigment project :)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need these things to get the project running on your local machine

```
- Python 3.6+
- Pip
```

### Create Virtual environment

```
mkvirtualenv clowningAround -p python3
```

### Installing

A step by step series of examples that tell you have to get a development env running

Install dependencies

```
pip install -r requirements/base.txt
```

Run migrations

```
python manage.py migrate
```

Run the project

```
python manage.py runserver
```

## Deployment

```TODO
frontend but not fully completed
url: http://127.0.0.1:8000/
```

## Login details

###backend details
url: http://127.0.0.1:8000/admin/login/?next=/admin/

- superuser
  username `siyabonga` password `siya`
- client
  username `Clients` password `siyabonga123`
- Clown
  username `Clowns` password `siyabonga123`
- Troupe_leader
  username `Troupe_leader` password `siyabonga123`

**Production notes**

    - ### Via admin site
        - Make sure you have access to the admin site. if not aks Siya to add you.

## Built With

- [Celery](http://docs.celeryproject.org/en/latest/index.html) - Distrubuted Task Management
- [Django](http://www.djangoproject.com/) - Web Framework
- [Django REST Framework](https://www.djangorestframework.org/) - Django REST Framework
