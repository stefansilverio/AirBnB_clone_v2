#!/usr/bin/python3
"""list cities"""
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def new_session(error):
    """remove current session"""
    storage.close()


@app.route('/states', defaults={'id': None}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def c(id):
    """send obj to jinja template"""
    all_states = storage.all(State)  # print all states if id not defined
    if id is None:
        return render_template('9-states.html', all_states=storage.all(State),
                               s_id=id)

    for city in all_states.values():
        if city.id == id:
            return render_template('9-states.html',
                                   all_states=storage.all(), s_id=id)

    return render_template('9-states.html', s_id=id)
    # id exists but state not found - print not found

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
