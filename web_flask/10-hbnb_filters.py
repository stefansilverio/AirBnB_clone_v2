#!/usr/bin/python3
"""list cities"""
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def new_session(error):
    """remove current session"""
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def display():
    """display html page"""
    return render_template('10-hbnb_filters.html', all_states=storage.all(State),
                           all_cities=storage.all(City),
                           all_amenities=storage.all(Amenity))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
