# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask, jsonify
import random

app = Flask(__name__)

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't programmers like nature? It has too many bugs.",
    "Why did the math book look sad? Because it had too many problems.",
    "What do you call fake spaghetti? An impasta!"
]

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/laugh', methods=['GET'])
def make_me_laugh():
    return jsonify({'joke': random.choice(jokes)})

if __name__ == '__main__':
    app.run()