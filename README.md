# Flask Hello World application
=============================

This is the Flask Hello World application shamelessly copied from
http://flask.pocoo.org/docs/quickstart/.

## New Feature: Laugh Endpoint

This application now includes an endpoint that returns a random joke to make you laugh!

## Endpoints

- `GET /`: Returns a simple "Hello, World!" message.
- `GET /laugh`: Returns a random joke.

## Installation

1. Clone the repository.
2. Install the required packages:
   ```bash
   pip install Flask
   ```
3. Run the application:
   ```bash
   python app.py
   ```

## Running Tests

To run the tests for the application, use the following command:
```bash
pytest
```

## License

This project is licensed under the MIT License.
```

```python
from flask import Flask, jsonify
import random

app = Flask(__name__)

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised!",
    "Why don't programmers like nature? It has too many bugs.",
    "What do you call fake spaghetti? An impasta!"
]

@app.route('/')
def hello():
    return "Hello, World!"

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

def test_hello(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'
    assert response.status_code == 200

def test_laugh(client):
    response = client.get('/laugh')
    assert response.status_code == 200
    assert 'joke' in response.json
    assert isinstance(response.json['joke'], str)