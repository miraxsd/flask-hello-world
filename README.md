Flask Hello World application
=============================

This is the Flask Hello World application shamelessly copied from
http://flask.pocoo.org/docs/quickstart/.

## Unit Tests

To separate the unit tests from the Flask server, create a new folder named `tests` in the root directory of the project. Place all unit test files in this folder.

### Directory Structure

/your_flask_app
│
├── app.py
├── tests/
│   ├── __init__.py
│   ├── test_app.py
│
└── README.md

### Required Packages for Unit Tests

Make sure to install the following packages for unit testing:

- pytest
- pytest-flask

You can install these packages using pip:

pip install pytest pytest-flask