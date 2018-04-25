#!/bin/sh
export FLASK_APP=./app/main.py
source $(pipenv --venv)/bin/activate
gunicorn -b :5000 -w 4 --chdir ./app main:app
flask run -h 0.0.0.0