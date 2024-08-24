from flask import Flask, jsonify
import requests

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

if __name__ == '__main__':
    app.run(debug=True, threaded=True)