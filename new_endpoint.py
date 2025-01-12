from flask import Flask, jsonify, request
import pytz
from datetime import datetime
import logging
import random

app = Flask(__name__)

@app.route('/api/v1/random_quote', methods=['GET'])
def random_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "Get busy living or get busy dying. - Stephen King",
        "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
        "Believe you can and you're halfway there. - Theodore Roosevelt"
    ]
    
    selected_quote = random.choice(quotes)
    return jsonify({"quote": selected_quote})

@app.route('/api/v1/current_hour', methods=['GET'])
def current_hour():
    country = request.args.get('country')
    if not validate_country_code(country):
        logging.error(f'Invalid country code: {country}')
        return create_error_response('Invalid country code', 400)

    try:
        timezone = pytz.timezone(country)
        current_time = datetime.now(timezone)
        return jsonify({"current_hour": current_time.strftime('%H:%M')})
    except Exception as e:
        logging.error(f'Error retrieving time for country code {country}: {str(e)}')
        return create_error_response('Error retrieving time', 500)

if __name__ == '__main__':
    app.run(debug=True)