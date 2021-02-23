# Barra API
Technical backend for Barra, a mobile applications featuring customized job offers.

## Requirements
* [Python 3.x+](https://www.python.org/downloads/)
* [PIP (Python Dependency Manager)](https://pip.pypa.io/en/stable/installing/)

## Installing dependencies
Install application dependencies with `pip install -r requirements.txt`.

## Quickstart the app
```bash
export FLASK_APP=wsgi.py 
python wsgi.py
```
## Upcoming features 
[x] Auto deletion of the expired job offers
[x] Parrelizing operations through multiprocessing
* Extensive unit and integration tests
* `/search` endpoint
* `/tag` endpoint
* `/admin` Dashboard 
* Containerize with Docker