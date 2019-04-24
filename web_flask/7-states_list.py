#!/usr/bin/python3
"""list all states"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)
all_states = storage.all(State)


@app.route('/states_list', strict_slashes=False)
def s():
    """show all states"""
    return render_template('7-states_list.html', state=all_states.values())


@app.teardown_appcontext
def new_session(all_states):
    """end current session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

