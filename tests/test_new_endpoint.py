import unittest
from app import app  # Assuming your Flask app is in app.py

class TestNewEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_new_endpoint_get(self):
        response = self.app.get('/new-endpoint')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Expected response content', response.data)

    def test_new_endpoint_post(self):
        response = self.app.post('/new-endpoint', json={'key': 'value'})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Success message', response.data)

    def test_new_endpoint_invalid_data(self):
        response = self.app.post('/new-endpoint', json={'invalid_key': 'value'})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Error message', response.data)

if __name__ == '__main__':
    unittest.main()