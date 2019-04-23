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
    text = text.replace("_", " ")
    return ("C {}".format(text))


@app.route('/python', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def p(text):
    """handle variable"""
    text = text.replace("_", " ")
    return ("Python {}".format(text))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
