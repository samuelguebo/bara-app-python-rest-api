# Barra API
Technical backend for Barra, a mobile applications featuring customized job offers.

## Requirements
* [Python 3.x+](https://www.python.org/downloads/)
* [PIP (Python Dependency Manager)](https://pip.pypa.io/en/stable/installing/)

## Installing dependencies
Install application dependencies with `pip install -r requirements.txt`.

## Handle Database migrations

```bash
alembic init alembic
alembic stamp head
alembic revision --autogenerate -m "Latest database upgrade"
alembic upgrade head
```

## Quickstart the app
```bash
export FLASK_APP=wsgi.py 
python wsgi.py
```
## Upcoming features 
* `/admin` Dashboard 
* Containerize with Docker