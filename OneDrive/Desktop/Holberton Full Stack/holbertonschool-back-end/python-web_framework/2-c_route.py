#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """ A function that displays hello """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ A function that displays HBNB """
    return 'HBNB'
@app.route('/c/<text>', strict_slashes=False)
def c_print(text):
    """ A function that returns a simple string """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)