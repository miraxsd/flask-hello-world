Flask Hello World application
=============================

This is the Flask Hello World application shamelessly copied from
http://flask.pocoo.org/docs/quickstart/.

## New Feature: Laugh Endpoint

We have added a new endpoint `/laugh` that returns a random joke to make you laugh!

### Laugh Endpoint

- **URL**: `/laugh`
- **Method**: `GET`
- **Response**: A JSON object containing a joke.

#### Example Response

```json
{
    "joke": "Why don't scientists trust atoms? Because they make up everything!"
}
```

## Running the Application

To run the application, use the following command:

```bash
flask run
```

## Running Tests

To run the tests for the new laugh endpoint, use the following command:

```bash
pytest
```

Make sure you have `pytest` installed in your environment.

## Contributing

If you have any jokes to add or improvements, feel free to contribute!

## License

This project is licensed under the MIT License - see the LICENSE file for details.