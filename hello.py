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

@app.route('/happy', methods=['GET'])
def happy_endpoint():
    return jsonify({'message': 'Happy coding!'}), 200

if __name__ == '__main__':
    app.run(debug=True, threaded=True)