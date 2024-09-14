import unittest
from hello import app  # Updated import to match the file name

class WeatherTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app  # Updated to use the app directly
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_hello(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello World!')  # Updated expected response

    def test_meteo_tataouine(self):
        response = self.client.get('/meteo/tataouine')
        self.assertEqual(response.status_code, 200)
        self.assertIn('temperature', response.json)
        self.assertIn('humidity', response.json)
        self.assertIn('description', response.json)

    def test_prayer_times_tataouine(self):
        response = self.client.get('/api/prayer-times?location=tataouine')  # Updated endpoint
        self.assertEqual(response.status_code, 200)
        self.assertIn('Fajr', response.json['prayer_times'])  # Updated keys to match the response
        self.assertIn('Dhuhr', response.json['prayer_times'])
        self.assertIn('Asr', response.json['prayer_times'])
        self.assertIn('Maghrib', response.json['prayer_times'])
        self.assertIn('Isha', response.json['prayer_times'])

    def test_news_headlines_country(self):
        country = 'your_country'  # Replace with the specific country
        response = self.client.get(f'/news/{country}')  # Updated endpoint
        self.assertEqual(response.status_code, 200)
        self.assertIn('headlines', response.json)
        self.assertIsInstance(response.json['headlines'], list)

if __name__ == '__main__':
    unittest.main()