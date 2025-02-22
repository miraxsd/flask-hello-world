import unittest
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/make_me_laugh', methods=['GET'])
def make_me_laugh():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "What do you call fake spaghetti? An impasta!"
    ]
    return jsonify({'joke': random.choice(jokes)})

class TestMakeMeLaughEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_make_me_laugh(self):
        response = self.app.get('/make_me_laugh')
        self.assertEqual(response.status_code, 200)
        self.assertIn('joke', response.get_json())

if __name__ == '__main__':
    unittest.main()