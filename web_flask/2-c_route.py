#!/usr/bin/python3
"""handle a variable"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """return text"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello():
    """return text"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """handle variable"""
    return "C %s" % text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
