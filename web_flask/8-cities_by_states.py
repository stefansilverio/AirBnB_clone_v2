#!/usr/bin/python3
"""list cities"""
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)
all_states = storage.all(State)

@app.teardown_appcontext
def new_session(error):
    """remove current session"""
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def c():
    """send obj to jinja template"""
    return render_template('8-cities_by_states.html', states=all_states.values())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
