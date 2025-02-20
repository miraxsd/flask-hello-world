# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask, request, jsonify
import inflect

app = Flask(__name__)
p = inflect.engine()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/convert', methods=['GET'])
def convert_number_to_text():
    number = request.args.get('number', type=int)
    if number is None:
        return jsonify({'error': 'No number provided'}), 400
    text = p.number_to_words(number)
    return jsonify({'number': number, 'text': text})

if __name__ == '__main__':
    app.run()