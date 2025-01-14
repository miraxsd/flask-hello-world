# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/celsius_to_fahrenheit')
def celsius_to_fahrenheit():
    celsius = request.args.get('celsius', type=float)
    if celsius is None:
        return "Please provide a 'celsius' query parameter", 400
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius} degrees Celsius is equivalent to {fahrenheit} degrees Fahrenheit."

if __name__ == '__main__':
    app.run()

