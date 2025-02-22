Flask Hello World application
=============================

This is the Flask Hello World application shamelessly copied from
http://flask.pocoo.org/docs/quickstart/.

## New Feature: Laugh Endpoint

This application now includes an endpoint that returns a random joke to make you laugh.

### Endpoints

- `GET /`: Returns a simple "Hello, World!" message.
- `GET /laugh`: Returns a random joke.

### Installation

1. Clone the repository.
2. Install the required packages:
   ```bash
   pip install Flask
   ```

### Running the Application

Run the application with:
```bash
python app.py
```

### Running Tests

To run the tests, use:
```bash
pytest test_app.py
```

### Example Usage

- Access the main page: `http://localhost:5000/`
- Access the laugh endpoint: `http://localhost:5000/laugh`
```

```python
# app.py
from flask import Flask, jsonify
import random

app = Flask(__name__)

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised!",
    "Why don't skeletons fight each other? They don't have the guts!"
]

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/laugh', methods=['GET'])
def laugh():
    return jsonify({'joke': random.choice(jokes)})

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello():
    response = client().get('/')
    assert response.data == b'Hello, World!'
    assert response.status_code == 200

def test_laugh():
    response = client().get('/laugh')
    assert response.status_code == 200
    assert 'joke' in response.get_json()