# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/laugh')
def make_me_laugh():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What do you call fake spaghetti? An impasta!"
    ]
    return jsonify({'joke': random.choice(jokes)})

if __name__ == '__main__':
    app.run()