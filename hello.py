from flask import Flask, jsonify, request
import requests
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/what')
def what_do_you_need():
    return "I need your instructions to complete the task!"

import os
import logging

API_KEY = os.getenv('OPENWEATHER_API_KEY', 'your_default_openweather_api_key')
NEWS_API_KEY = os.getenv('NEWS_API_KEY', 'your_default_news_api_key')

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
ERROR_CITY_NOT_FOUND = 'Invalid city name'

logging.basicConfig(level=logging.DEBUG)

def handle_api_error(response):
    """Handle API errors and return structured JSON response."""
    if response.status_code == 404:
        logging.error('Resource not found')
        return create_error_response('Resource not found', 404)
    elif response.status_code == 401:
        logging.error('Unauthorized access')
        return create_error_response('Unauthorized access', 401)
    else:
        logging.error(f'Unexpected error occurred: {response.status_code}')
        return create_error_response('An unexpected error occurred', response.status_code)

@app.route('/api/weather/<city>', methods=['GET'])
def get_weather_by_city(city):
    """Get weather information for a specific city."""
    if not validate_city_name(city):
        logging.error(f'Invalid city name: {city}')
        return create_error_response(ERROR_CITY_NOT_FOUND, 400)
    logging.info(f'Fetching weather data for city: {city}')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    
    response = requests.get(url)
    data = response.json()
    
    logging.debug(f'Response from weather API for city {city}: {data}')

    if response.status_code == 200:
        meteo_info = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return jsonify({'data': meteo_info}), 200
    else:
        return handle_api_error(response)

@app.route('/api/prayer-times', methods=['GET'])
def get_prayer_times():
    """Get prayer times based on location and optional date."""
    date = request.args.get('date')
    if date and not validate_date_format(date):
        return create_error_response('Invalid date format, use YYYY-MM-DD', 400)
    location = request.args.get('location')
    date = request.args.get('date')
    
    if not location:
        logging.error('Location parameter is required.')
        return create_error_response('Location parameter is required', 400)
    logging.info(f'Fetching prayer times for location: {location}')

    prayer_times_data = {
        'Fajr': '05:00',
        'Dhuhr': '12:00',
        'Asr': '15:30',
        'Maghrib': '18:00',
        'Isha': '19:30'
    }
    
    return jsonify({
        'data': {
            'location': location,
            'date': date or datetime.now(pytz.timezone('UTC')).date().isoformat(),
            'prayer_times': prayer_times_data
        }
    }), 200

@app.route('/api/news/<country>', methods=['GET'])
def get_news_headlines(country):
    if not validate_country_code(country):
        logging.error(f'Invalid country code: {country}')
        return create_error_response('Invalid country code', 400)
    logging.info(f'Fetching news headlines for country: {country}')
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
    
    response = requests.get(url)
    data = response.json()
    
    logging.debug(f'Response from news API for country {country}: {data}')
    
    if response.status_code == 200 and data.get('articles'):
        headlines = [{'title': article['title'], 'url': article['url']} for article in data['articles']]
        return jsonify({'data': headlines}), 200
    else:
        return handle_api_error(response)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)