from flask import Flask, request, jsonify
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/api/prayer-times', methods=['GET'])
def prayer_times():
    location = request.args.get('location')
    date = request.args.get('date', datetime.now().strftime('%Y-%m-%d'))

    # Replace with actual logic to retrieve prayer times
    # For demonstration, we use a dummy response
    prayer_times_data = {
        'location': location,
        'date': date,
        'fajr': '05:00',
        'dhuhr': '12:00',
        'asr': '15:00',
        'maghrib': '18:00',
        'isha': '19:30'
    }

    return jsonify(prayer_times_data)

if __name__ == '__main__':
    app.run(debug=True)