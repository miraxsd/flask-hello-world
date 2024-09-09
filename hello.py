# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/greet/<name>')
def greet(name):
    return jsonify(message=f'Hello, {name}! Welcome to our API.')

if __name__ == '__main__':
    app.run()