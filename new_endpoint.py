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

if __name__ == '__main__':
    app.run(debug=True)