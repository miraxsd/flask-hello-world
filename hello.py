from flask import Flask, jsonify, request
import requests
from datetime import datetime
import pytz
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model for SaaS subscription management
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    subscription_active = db.Column(db.Boolean, default=False)

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

@app.route('/api/register', methods=['POST'])
def register_user():
    data = request.json
    email = data.get('email')
    
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    
    user = User(email=email, subscription_active=False)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/api/subscribe/<int:user_id>', methods=['POST'])
def subscribe_user(user_id):
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    user.subscription_active = True
    db.session.commit()
    
    return jsonify({'message': 'Subscription activated successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, threaded=True)