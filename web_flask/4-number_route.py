#!/usr/bin/python3
"""Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route function to handle requests to the root URL."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route function to handle requests to the '/hbnb' URL."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Route function to handle requests to the '/c/<text>' URL."""
    t = text.replace('_', ' ')
    return 'C {}'.format(t)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Route function to handle requests to the '/python/<text>' URL."""
    t = text.replace('_', ' ')
    return 'Python {}'.format(t)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Route function to handle requests to the '/number/<n>' URL."""
    number = str(n)
    return '{} is a number'.format(number)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
