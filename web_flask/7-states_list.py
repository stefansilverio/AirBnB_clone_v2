#!/usr/bin/python3
"""list all states"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def new_session(error):
    """end current session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def s():
    """show all states"""
    all_states = storage.all(State)
    return render_template('7-states_list.html', state=all_states.values())


if __name__ == "__main__":
    storage.close()
    app.run(host="0.0.0.0", port=5000)
