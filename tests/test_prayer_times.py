import unittest
from app import create_app

class TestPrayerTimesEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
    
    def test_get_prayer_times_valid_location(self):
        response = self.client.get('/api/prayer-times?location=Mecca&date=2023-10-01')
        self.assertEqual(response.status_code, 200)
        self.assertIn('fajr', response.json)
        self.assertIn('dhuhr', response.json)
        self.assertIn('asr', response.json)
        self.assertIn('maghrib', response.json)
        self.assertIn('isha', response.json)

    def test_get_prayer_times_invalid_location(self):
        response = self.client.get('/api/prayer-times?location=InvalidLocation&date=2023-10-01')
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.json)

    def test_get_prayer_times_missing_parameters(self):
        response = self.client.get('/api/prayer-times?location=Mecca')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    def test_get_prayer_times_invalid_date_format(self):
        response = self.client.get('/api/prayer-times?location=Mecca&date=01-10-2023')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    def test_get_prayer_times_no_auth_required(self):
        response = self.client.get('/api/prayer-times?location=Mecca&date=2023-10-01')
        self.assertEqual(response.status_code, 200)

    def test_get_news_headlines_valid_country(self):
        response = self.client.get('/api/news-headlines?country=SaudiArabia')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json.get('headlines'), list)

    def test_get_news_headlines_invalid_country(self):
        response = self.client.get('/api/news-headlines?country=InvalidCountry')
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.json)

    def test_get_news_headlines_missing_parameters(self):
        response = self.client.get('/api/news-headlines')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()