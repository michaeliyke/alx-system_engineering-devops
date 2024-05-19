#!/usr/bin/env bash
#+ # Script to start the gunicorn server serving task 0 of web_flask
#+ # Environment variables here
HBNB_ENV=test
HBNB_MYSQL_USER=hbnb_test
HBNB_MYSQL_PWD=hbnb_test_pwd
HBNB_MYSQL_HOST=localhost
HBNB_MYSQL_DB=hbnb_test_db
HBNB_TYPE_STORAGE=db

gunicorn --bind 0.0.0.0:5003 web_dynamic.2-hbnb:app

