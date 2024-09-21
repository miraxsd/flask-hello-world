import unittest
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/funny', methods=['GET'])
def funny_endpoint():
    return jsonify({"joke": "Why don't scientists trust atoms? Because they make up everything!"})

class TestFunnyEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_funny_endpoint(self):
        response = self.app.get('/funny')
        self.assertEqual(response.status_code, 200)
        self.assertIn('joke', response.json)
        self.assertEqual(response.json['joke'], "Why don't scientists trust atoms? Because they make up everything!")

if __name__ == '__main__':
    unittest.main()