from flask import Flask, jsonify
import random
import logging

app = Flask(__name__)

@app.route('/')
def hello_world() -> str:
    """Return a friendly greeting."""
    return 'Hello, World!'

@app.route('/laugh')
def make_me_laugh() -> str:
    """Return a random joke as a JSON response.

    Returns:
        str: A JSON formatted joke.

    Raises:
        Exception: If an error occurs while retrieving a joke.
    """
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my computer I needed a break, and now it won't stop sending me beach wallpapers."
    ]
    
    try:
        if not jokes:
            return jsonify({"success": False, "message": "No jokes available."})
        return jsonify(random.choice(jokes))
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({"success": False, "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)