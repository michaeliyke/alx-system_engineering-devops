#!/usr/bin/env bash
# Script to start the gunicorn server serving task 6 of web_flask
gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app

