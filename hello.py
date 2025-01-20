# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello_dumb')
def hello_dumb():
    return "Hello, I'm dumb!"

if __name__ == '__main__':
    app.run()

