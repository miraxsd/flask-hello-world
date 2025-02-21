import unittest
from your_flask_app import app  # Replace 'your_flask_app' with the actual name of your Flask app

class TestConversion(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_minutes_to_seconds(self):
        response = self.app.get('/convert/minutes_to_seconds?minutes=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'seconds': 300})

        response = self.app.get('/convert/minutes_to_seconds?minutes=0')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'seconds': 0})

        response = self.app.get('/convert/minutes_to_seconds?minutes=-1')
        self.assertEqual(response.status_code, 400)  # Assuming negative minutes should return a bad request

if __name__ == '__main__':
    unittest.main()