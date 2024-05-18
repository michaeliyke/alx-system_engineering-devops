#!/usr/bin/env bash
# Script to start the gunicorn server serving task 0 of web_flask
gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app

