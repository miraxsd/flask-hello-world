# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/convert_minutes_to_seconds', methods=['GET'])
def convert_minutes_to_seconds():
    minutes = request.args.get('minutes', default=0, type=int)
    seconds = minutes * 60
    return jsonify({'minutes': minutes, 'seconds': seconds})

if __name__ == '__main__':
    app.run()