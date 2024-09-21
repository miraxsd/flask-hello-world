import unittest
from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/funny', methods=['GET'])
def funny():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised!",
        "Why don't programmers like nature? It has too many bugs.",
        "Why did the math book look sad? Because it had too many problems."
    ]
    return jsonify({'joke': random.choice(jokes)})

class TestFunnyEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_funny_joke(self):
        response = self.app.get('/funny')
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertIn('joke', json_data)
        self.assertIsInstance(json_data['joke'], str)

if __name__ == '__main__':
    unittest.main()