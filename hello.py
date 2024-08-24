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
    # Replace 'YOUR_API_KEY' with your actual API key
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
    
    # Dummy data for prayer times, replace with your actual calculation or API call
    prayer_times_data = {
        'Fajr': '05:00',
        'Dhuhr': '12:00',
        'Asr': '15:30',
        'Maghrib': '18:00',
        'Isha': '19:30'
    }
    
    # Here you would implement the logic to calculate or fetch actual prayer times based on the location and date
    
    return jsonify({
        'location': location,
        'date': date or datetime.now(pytz.timezone('UTC')).date().isoformat(),
        'prayer_times': prayer_times_data
    }), 200

if __name__ == '__main__':
    app.run(debug=True, threaded=True)