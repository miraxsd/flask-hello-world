import unittest
from your_flask_app import create_app

class WeatherTestCase(unittest.TestCase):
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
        self.assertIn('temperature', response.json)
        self.assertIn('humidity', response.json)
        self.assertIn('description', response.json)

    def test_prayer_times_tataouine(self):
        response = self.client.get('/prayer_times/tataouine')
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

    def test_sad_endpoint(self):
        response = self.client.get('/sad')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Sadness is a part of life.')

if __name__ == '__main__':
    unittest.main()