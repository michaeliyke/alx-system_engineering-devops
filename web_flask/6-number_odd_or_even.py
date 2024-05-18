#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from markupsafe import escape

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


@app.route("/python/")  # This route fosters the behavior of a default value
@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    """ To display a variable: python is cool!"""
    text = escape(text.replace("_", " "))
    return f"Python {text}"


# Here default is not used, so the variable is required
@app.route("/c/<text>")
def isfun(text):
    """ To display a variable in the url"""
    return f"C {escape(text.replace('_', ' '))}"


@app.route('/user/<username>/')
@app.route('/user/<username>/<path:subpath>')
def show_user(username, subpath=None):
    """Optionally, a path can be added to the username."""
    if subpath:
        return f'User {username}, Subpath: {subpath}'
    else:
        return f'User {username}'


@app.route('/number/<int:n>')  # This route only accepts integer
def show_num(n):
    """ display “n is a number” only if n is an integer"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>')  # This route only accepts integer
def show_html(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')  # This route only accepts integer
def show_html_is_odd(n):
    """display a HTML page only if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

