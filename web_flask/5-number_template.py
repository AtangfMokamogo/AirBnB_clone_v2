#!/usr/bin/python3
""" Implements a Flask Web App on 0.0.0.0
                                port 5000
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns Hello HBNB from '/' route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB from '/hbnb' route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """This displays the value 'C'
        Followed by the value passed in <text> variable"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Returns Python followed by the value in <text> variable
        If no value is passed the URL returns Python followed by default
        value 'is cool'
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Return 'n is an integer
        ONLY if n is an integer
    """
    return '{} is an integer'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Return an HTML file,
        If n is an integer
    """
    return render_template('number_template.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
