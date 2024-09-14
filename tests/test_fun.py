import unittest
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/fun', methods=['GET'])
def fun_endpoint():
    return jsonify({"message": "This is a fun endpoint!"})

class TestFunEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_fun_endpoint(self):
        response = self.app.get('/fun')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "This is a fun endpoint!"})

if __name__ == '__main__':
    unittest.main()