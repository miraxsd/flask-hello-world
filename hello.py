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

@app.route('/meteo/tataouine')
def get_meteo_tataouine():
    api_key = 'YOUR_API_KEY'
    url = f'http://api.openweathermap.org/data/2.5/weather?q=Tataouine&appid={api_key}&units=metric'
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        meteo_info = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return jsonify(meteo_info), 200
    else:
        return jsonify({'error': 'City not found or API error'}), 404

@app.route('/api/prayer-times', methods=['GET'])
def get_prayer_times():
    location = request.args.get('location')
    date = request.args.get('date')
    
    if not location:
        return jsonify({'error': 'Location parameter is required'}), 400
    
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

@app.route('/news/<country>', methods=['GET'])
def get_news_headlines(country):
    api_key = 'YOUR_NEWS_API_KEY'  # Replace with your actual News API key
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200 and data.get('articles'):
        headlines = [{'title': article['title'], 'url': article['url']} for article in data['articles']]
        return jsonify({'headlines': headlines}), 200
    else:
        return jsonify({'error': 'Country not found or API error'}), 404

@app.route('/api/crime/<country>/<int:year>', methods=['GET'])
def get_crime_numbers(country, year):
    # Placeholder for crime data retrieval logic
    # In a real application, you would connect to a database or an external API to get the crime data
    crime_data = {
        'USA': {
            2020: 15000,
            2021: 16000,
            2022: 15500
        },
        'UK': {
            2020: 5000,
            2021: 5500,
            2022: 5300
        }
    }
    
    country_data = crime_data.get(country)
    
    if country_data and year in country_data:
        return jsonify({'country': country, 'year': year, 'crime_number': country_data[year]}), 200
    else:
        return jsonify({'error': 'Data not found for the specified country and year'}), 404

if __name__ == '__main__':
    app.run(debug=True, threaded=True)