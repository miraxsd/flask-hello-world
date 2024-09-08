import unittest
from flask import Flask, jsonify
from flask_testing import TestCase

app = Flask(__name__)

# Sample data for testing
crime_data = {
    'USA': {
        '2020': 1500000,
        '2021': 1600000,
        '2022': 1550000,
    },
    'Canada': {
        '2020': 500000,
        '2021': 510000,
        '2022': 520000,
    }
}

@app.route('/crime/<country>/<year>', methods=['GET'])
def get_crime_number(country, year):
    if country in crime_data and year in crime_data[country]:
        return jsonify({year: crime_data[country][year]}), 200
    return jsonify({'error': 'Data not found'}), 404

class TestCrimeEndpoint(TestCase):
    def create_app(self):
        return app

    def test_crime_number_found(self):
        response = self.client.get('/crime/USA/2021')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'2021': 1600000})

    def test_crime_number_not_found_country(self):
        response = self.client.get('/crime/Unknown/2021')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'error': 'Data not found'})

    def test_crime_number_not_found_year(self):
        response = self.client.get('/crime/Canada/2019')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'error': 'Data not found'})

if __name__ == '__main__':
    unittest.main()