import unittest
from your_flask_app import create_app

class SaaSTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_hello(self):
        response = self.client.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

    def test_meteo_city(self):
        city = 'tataouine'
        response = self.client.get(f'/meteo/{city}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('temperature', response.json)
        self.assertIn('humidity', response.json)
        self.assertIn('description', response.json)

    def test_prayer_times_city(self):
        city = 'tataouine'
        response = self.client.get(f'/prayer_times/{city}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('fajr', response.json)
        self.assertIn('dhuhr', response.json)
        self.assertIn('asr', response.json)
        self.assertIn('maghrib', response.json)
        self.assertIn('isha', response.json)

    def test_news_headlines_country(self):
        country = 'your_country'  # Replace with the specific country
        response = self.client.get(f'/news/headlines/{country}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('headlines', response.json)
        self.assertIsInstance(response.json['headlines'], list)

    def test_user_signup(self):
        response = self.client.post('/signup', json={
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('token', response.json)

    def test_user_login(self):
        response = self.client.post('/login', json={
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json)

if __name__ == '__main__':
    unittest.main()