Flask Hello World application
=============================

This is the Flask Hello World application shamelessly copied from
http://flask.pocoo.org/docs/quickstart/.

## New Feature: Laugh Endpoint

This application now includes an endpoint that returns a random joke to make you laugh.

### Endpoints

- `GET /`: Returns a simple Hello World message.
- `GET /laugh`: Returns a random joke.

### Running the Application

To run the application, use the following command:

```bash
flask run
```

### Testing the Application

To run the tests, use the following command:

```bash
pytest
```

### Dependencies

Make sure to install the required dependencies:

```bash
pip install Flask pytest
```
```

```python
from flask import Flask, jsonify
import random

app = Flask(__name__)

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised!",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call fake spaghetti? An impasta!"
]

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/laugh')
def laugh():
    return jsonify(joke=random.choice(jokes))

if __name__ == '__main__':
    app.run(debug=True)
```

```python
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'
    assert response.status_code == 200

def test_laugh(client):
    response = client.get('/laugh')
    assert response.status_code == 200
    assert b'joke' in response.get_json()
    assert isinstance(response.get_json()['joke'], str)