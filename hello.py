# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/convert_time', methods=['GET'])
def convert_time():
    hours = request.args.get('hours', type=float)
    if hours is None:
        return jsonify({'error': 'Please provide hours as a query parameter.'}), 400
    seconds = hours * 3600
    return jsonify({'seconds': seconds})

if __name__ == '__main__':
    app.run()