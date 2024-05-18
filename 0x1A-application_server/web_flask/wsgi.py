#!/usr/bin/python3
"""This is the WSGI file for the app"""

app = __import__('web_flask.0-hello_route').app

if __name__ == '__main__':
    app.run()
