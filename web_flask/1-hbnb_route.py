#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False  # Turn off strict slash checks


@app.route("/")
def index():
    """The hello world route"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ To display HBNB on the /hbnb route"""
    return "HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

