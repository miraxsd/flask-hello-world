from flask import Flask, jsonify, request

app = Flask(__name__)

# Global list to hold book names
book_names = []

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/what')
def what_do_you_need():
    return "I need your instructions to complete the task!"

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(book_names)

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json.get('name')
    if new_book:
        book_names.append(new_book)
        return jsonify({'message': 'Book added successfully!'}), 201
    return jsonify({'message': 'Book name is required!'}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

Unit tests (create a new file `test_hello.py`):
```python
import unittest
import json
from hello import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.data, b'Hello World!')

    def test_what_do_you_need(self):
        response = self.app.get('/what')
        self.assertEqual(response.data, b'I need your instructions to complete the task!')

    def test_get_books(self):
        response = self.app.get('/books')
        self.assertEqual(response.json, [])

    def test_add_book(self):
        response = self.app.post('/books', json={'name': 'The Great Gatsby'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Book added successfully!')

        response = self.app.get('/books')
        self.assertEqual(response.json, ['The Great Gatsby'])

    def test_add_book_without_name(self):
        response = self.app.post('/books', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'Book name is required!')

if __name__ == '__main__':
    unittest.main()