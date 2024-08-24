from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/what')
def what_do_you_need():
    return "I need your instructions to complete the task!"

@app.route('/meteo/<city>')
def get_meteo(city):
    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = 'YOUR_API_KEY'
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()
    
    if weather_response.status_code == 200:
        meteo_info = {
            'city': city,
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'humidity': weather_data['main']['humidity'],
            'wind_speed': weather_data['wind']['speed']
        }
    else:
        return jsonify({'error': 'City not found or API error'}), 404

    # Fetch prayer times
    prayer_url = f'http://api.aladhan.com/v1/timingsByCity?city={city}&country=your_country'  # Replace 'your_country' with appropriate country
    prayer_response = requests.get(prayer_url)
    prayer_data = prayer_response.json()
    
    if prayer_response.status_code == 200:
        prayer_times = {
            'fajr': prayer_data['data']['timings']['Fajr'],
            'dhuhr': prayer_data['data']['timings']['Dhuhr'],
            'asr': prayer_data['data']['timings']['Asr'],
            'maghrib': prayer_data['data']['timings']['Maghrib'],
            'isha': prayer_data['data']['timings']['Isha']
        }
    else:
        prayer_times = {'error': 'Could not fetch prayer times'}

    meteo_info['prayer_times'] = prayer_times
    return jsonify(meteo_info), 200

if __name__ == '__main__':
    app.run(debug=True, threaded=True)