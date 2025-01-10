from flask import Flask, jsonify, request
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

@app.route('/api/v1/population/<country>', methods=['GET'])
def population(country):
    populations = {
        "USA": 331002651,
        "Canada": 37742154,
        "UK": 67886011,
        "Germany": 83783942,
        "France": 65273511,
        "India": 1380004385,
        "China": 1439323776
    }
    
    country_population = populations.get(country)
    if country_population:
        return jsonify({"country": country, "population": country_population})
    else:
        return jsonify({"error": "Country not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)