import unittest
from app import create_app

class TestNewEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_new_endpoint_success(self):
        response = self.client.get('/api/new-endpoint')
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.json)

    def test_new_endpoint_not_found(self):
        response = self.client.get('/api/nonexistent-endpoint')
        self.assertEqual(response.status_code, 404)

    def test_new_endpoint_invalid_method(self):
        response = self.client.post('/api/new-endpoint')
        self.assertEqual(response.status_code, 405)

    def test_new_endpoint_query_param(self):
        response = self.client.get('/api/new-endpoint?param=value')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['param'], 'value')

    def test_new_endpoint_authentication(self):
        response = self.client.get('/api/new-endpoint', headers={'Authorization': 'Bearer invalid_token'})
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()