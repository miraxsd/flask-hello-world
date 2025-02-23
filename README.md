Flask Hello World application
=============================

This is the Flask Hello World application shamelessly copied from
http://flask.pocoo.org/docs/quickstart/.

Adding a Laugh Endpoint
------------------------
We have added a new endpoint `/laugh` that returns a random joke to make you laugh. 

### Endpoint
- **GET /laugh**
  - Returns a random joke in JSON format.

### Example Response
```json
{
  "joke": "Why don't scientists trust atoms? Because they make up everything!"
}
```

Testing the Laugh Endpoint
---------------------------
To ensure the `/laugh` endpoint works correctly, we have included tests using `unittest`. 

### Running Tests
To run the tests, execute the following command:
```bash
python -m unittest discover
```

### Test Cases
- Test that the `/laugh` endpoint returns a 200 status code.
- Test that the response contains a joke in JSON format.

Installation
------------
To install the required packages, run:
```bash
pip install -r requirements.txt
```

Usage
-----
To run the application, use:
```bash
flask run
```

Now you can access the application at `http://127.0.0.1:5000` and make a request to the `/laugh` endpoint to get a joke!