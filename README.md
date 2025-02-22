Flask Hello World application
=============================

This is the Flask Hello World application shamelessly copied from
http://flask.pocoo.org/docs/quickstart/.

Add a Laugh Endpoint
---------------------
This application now includes an endpoint that returns a random joke to make you laugh. 

### Endpoints
- `GET /`: Returns a simple "Hello, World!" message.
- `GET /laugh`: Returns a random joke.

### Installation
1. Clone the repository.
2. Navigate to the project directory.
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
To run the application, use the following command:
```bash
flask run
```

### Running Tests
To run the tests for the application, use:
```bash
pytest
```

### Dependencies
- Flask
- Flask-Testing
- Any other dependencies listed in `requirements.txt`

### Contributing
Feel free to submit issues or pull requests for improvements or additional features.