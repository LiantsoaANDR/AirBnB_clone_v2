#!/usr/bin/python3
"""
Start a Flask web application

/:  display Hello HBNB!
/hbnb:  display HBNB
/c/<text>:  display C, followed by the value of the text variable
            (replace underscore _ symbols with a space )
/python/(<text>): display Python, followed by the value of the text variable
                  (replace underscore _ symbols with a space )
                  The default value of text is 'is cool'
/number/<n>:    display 'n is a number' only if n is an integer
/number_template/<n>:   display a HTML page only if n is an integer:
                        H1 tag: 'Number: n' inside the tag BODY
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route function, handle requests to the root URL"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Handle request on /hbnb, return 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text():
    """Handle request on /c/<text>, return 'C' + text ('_' replaced by ' ')"""
    t = text.replace('_', ' ')
    return 'C {}'.format(t)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Handle request on /python and /python/<text>
    Return 'Python' + text ('_' replace by ' '), default value: 'is cool'
    """
    t = text.replace('_', ' ')
    return 'Python {}'.format(t)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Handle request on /number/<n>. return: 'n is a number'"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template():
    """
    Handle request on /number_template/<n>.
    return a HTML page only if n is an int
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
