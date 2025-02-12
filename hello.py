from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/convert', methods=['GET'])
def convert_celsius_to_fahrenheit():
    celsius = request.args.get('celsius', type=float)
    if celsius is None:
        return jsonify({'error': 'Please provide a valid Celsius value.'}), 400
    fahrenheit = (celsius * 9/5) + 32
    return jsonify({'celsius': celsius, 'fahrenheit': fahrenheit})

if __name__ == '__main__':
    app.run()