# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def hello_world() -> str:
    """Return a friendly greeting.

    Returns:
        str: A greeting message.
    """
    return 'Hello World!'

@app.route('/laugh')
def make_me_laugh() -> str:
    """Return a random joke to make you laugh.

    Returns:
        str: A random joke.

    Raises:
        Exception: If there is an issue retrieving a joke.
    """
    jokes: list[str] = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised!",
        "Why don't skeletons fight each other? They don't have the guts!"
    ]

    try:
        return random.choice(jokes)
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run()