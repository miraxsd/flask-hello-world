# Project Documentation

## Overview

This project includes a fun API that provides various endpoints for users to interact with. One of the key features is the "Make Me Laugh" endpoint, which returns a random joke to lighten the mood.

## Endpoints

### GET /laugh

- **Description**: Returns a random joke to make you laugh.
- **Response**:
  - **200 OK**: A JSON object containing a joke.
    ```json
    {
      "joke": "Why don't scientists trust atoms? Because they make up everything!"
    }
    ```
  - **500 Internal Server Error**: If there is an issue retrieving the joke.

## Example Request

```bash
curl -X GET http://localhost:3000/laugh
```

## Running Tests

To ensure the functionality of the "Make Me Laugh" endpoint, tests have been implemented. You can run the tests using the following command:

```bash
npm test
```

### Test Cases

1. **Test for successful response**:
   - **Description**: Ensure that the /laugh endpoint returns a 200 status code and a joke.
   - **Expected Outcome**: The response should contain a JSON object with a "joke" key.

2. **Test for error handling**:
   - **Description**: Simulate an error when fetching a joke and ensure the endpoint returns a 500 status code.
   - **Expected Outcome**: The response should indicate an internal server error.

## Contribution

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure that you include tests for any new features or changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.