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

API_KEY = os.getenv('OPENWEATHER_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
ERROR_CITY_NOT_FOUND = 'Invalid city name'

logging.basicConfig(level=logging.INFO)

def create_error_response(message, status_code):
    """Create a uniform error response."""
    return jsonify({'error': message}), status_code

@app.route('/api/weather/<city>', methods=['GET'])
def get_weather_by_city(city):
    if not validate_city_name(city):
        return create_error_response(ERROR_CITY_NOT_FOUND, 400)
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    
    response = requests.get(url)
    data = response.json()
    
    logging.info(f'Response from weather API for city {city}: {data}')

    if response.status_code == 200:
        meteo_info = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return jsonify(meteo_info), 200
    else:
        return handle_api_error(response)

@app.route('/api/prayer-times', methods=['GET'])
def get_prayer_times():
    """Get prayer times based on location and optional date."""
    location = request.args.get('location')
    date = request.args.get('date')
    
    if not location:
        return create_error_response('Location parameter is required', 400)

    prayer_times_data = {
        'Fajr': '05:00',
        'Dhuhr': '12:00',
        'Asr': '15:30',
        'Maghrib': '18:00',
        'Isha': '19:30'
    }
    
    return jsonify({
        'location': location,
        'date': date or datetime.now(pytz.timezone('UTC')).date().isoformat(),
        'prayer_times': prayer_times_data
    }), 200
    
    return jsonify({
        'location': location,
        'date': date or datetime.now(pytz.timezone('UTC')).date().isoformat(),
        'prayer_times': prayer_times_data
    }), 200

@app.route('/news/<country>', methods=['GET'])
def get_news_headlines(country):
    if not validate_country_code(country):
        return jsonify({'error': 'Invalid country code'}), 400
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}'
    
    response = requests.get(url)
    data = response.json()
    
    logging.info(f'Response from news API for country {country}: {data}')
    
    if response.status_code == 200 and data.get('articles'):
        headlines = [{'title': article['title'], 'url': article['url']} for article in data['articles']]
        return jsonify({'headlines': headlines}), 200
    else:
        return handle_api_error(response)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)