# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/convert/celsius_to_fahrenheit', methods=['GET'])
def convert_celsius_to_fahrenheit():
    celsius = request.args.get('celsius', type=float)
    if celsius is None:
        return jsonify({'error': 'Please provide a Celsius value.'}), 400
    fahrenheit = (celsius * 9/5) + 32
    return jsonify({'celsius': celsius, 'fahrenheit': fahrenheit})

@app.route('/convert/fahrenheit_to_celsius', methods=['GET'])
def convert_fahrenheit_to_celsius():
    fahrenheit = request.args.get('fahrenheit', type=float)
    if fahrenheit is None:
        return jsonify({'error': 'Please provide a Fahrenheit value.'}), 400
    celsius = (fahrenheit - 32) * 5/9
    return jsonify({'fahrenheit': fahrenheit, 'celsius': celsius})

if __name__ == '__main__':
    app.run()