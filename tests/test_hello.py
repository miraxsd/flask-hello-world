import unittest
from your_flask_app import create_app

class WeatherTestCase(unittest.TestCase):
    """Unit tests for the weather-related endpoints in the Flask application."""

    def setUp(self):
        """Set up the test client before each test."""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_hello(self):
        """Test the /hello endpoint to ensure it returns a greeting."""
        response = self.client.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

    def test_meteo_tataouine(self):
        """Test the /meteo/tataouine endpoint to check for weather data."""
        response = self.client.get('/meteo/tataouine')
        self.assertEqual(response.status_code, 200)
        self.assertIn('temperature', response.json)
        self.assertIn('humidity', response.json)
        self.assertIn('description', response.json)

    def test_prayer_times_tataouine(self):
        """Test the /prayer_times/tataouine endpoint to verify prayer times."""
        response = self.client.get('/prayer_times/tataouine')
        self.assertEqual(response.status_code, 200)
        self.assertIn('fajr', response.json)
        self.assertIn('dhuhr', response.json)
        self.assertIn('asr', response.json)
        self.assertIn('maghrib', response.json)
        self.assertIn('isha', response.json)

    def test_news_headlines_country(self):
        """Test the /news/headlines/{country} endpoint to ensure it returns news headlines."""
        country = 'your_country'  # Replace with the specific country
        response = self.client.get(f'/news/headlines/{country}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('headlines', response.json)
        self.assertIsInstance(response.json['headlines'], list)

if __name__ == '__main__':
    unittest.main()