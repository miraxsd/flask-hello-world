@app.route('/api/viral-films', methods=['GET'])
def get_viral_films():
    api_key = 'YOUR_MOVIE_API_KEY'  # Replace with your actual movie API key
    url = f'https://api.themoviedb.org/3/trending/movie/week?api_key={api_key}'
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200 and data.get('results'):
        viral_films = [{'title': film['title'], 'popularity': film['popularity']} for film in data['results']]
        return jsonify({'viral_films': viral_films}), 200
    else:
        return jsonify({'error': 'Error fetching viral films'}), 404