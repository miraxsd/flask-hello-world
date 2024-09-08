import random

@app.route('/random', methods=['GET'])
def get_random_number():
    random_number = random.randint(5, 10)
    return jsonify({'random_number': random_number}), 200