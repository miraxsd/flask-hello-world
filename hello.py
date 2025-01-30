from flask import Flask
import logging

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello_simple')
def hello_simple():
    """Return a simple greeting."""
    try:
        return "Hello, I'm simple!"
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return "An error occurred while processing your request."

if __name__ == '__main__':
    app.run()