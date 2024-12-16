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

@app.route('/api/v1/noob_welcome', methods=['GET'])
def noob_welcome():
    return jsonify({"message": "Welcome to our API! We're glad to have you here."})

@app.route('/api/v1/noob_tips', methods=['GET'])
def noob_tips():
    tips = [
        "Start with the fundamentals: Understand the basics of programming languages and computer science concepts.",
        "Practice, practice, practice: Build small projects to apply what you've learned.",
        "Read code written by others: It will help you understand different styles and approaches.",
        "Don't hesitate to ask for help: Join communities and forums.",
        "Keep learning: Technology changes rapidly, stay updated with new tools and techniques."
    ]
    return jsonify({"tips": tips})