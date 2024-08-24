import unittest
from your_flask_app import create_app

class HelloWorldTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_hello(self):
        response = self.client.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

    def test_meteo_tataouine(self):
        response = self.client.get('/meteo/tataouine')
        self.assertEqual(response.status_code, 200)
        # Assuming the expected response is a JSON object
        self.assertIn('temperature', response.json)
        self.assertIn('humidity', response.json)
        self.assertIn('description', response.json)

if __name__ == '__main__':
    unittest.main()