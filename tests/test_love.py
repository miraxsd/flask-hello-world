import unittest
from app import create_app

class TestLoveEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_love_endpoint(self):
        response = self.client.get('/love')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Love is in the air', response.data)

    def test_love_endpoint_json(self):
        response = self.client.get('/love', headers={'Accept': 'application/json'})
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertEqual(json_data['message'], 'Love is in the air')

if __name__ == '__main__':
    unittest.main()