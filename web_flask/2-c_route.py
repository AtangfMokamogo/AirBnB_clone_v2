#!/usr/bin/python3
""" Implements a Flask Web App on 0.0.0.0
                                port 5000
"""
from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
