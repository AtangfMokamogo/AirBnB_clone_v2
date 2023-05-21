#!/usr/bin/python3
"""Implements a basic Flask Web App"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Destroy the current SQLAlchemy session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """Display an HTML page listing states
        sorted in alphabetical order
        """
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """Returns html page with state id if present"""

    state = storage.get("State", id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
