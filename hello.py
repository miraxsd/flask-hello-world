```python
# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/what')
def what_do_you_need():
    return "I need your instructions to complete the task!"

if __name__ == '__main__':
    app.run()
```

**Explanation:**

1. **Import Flask:**  We import the Flask class to create our web application.
2. **Create Flask App:** `app = Flask(__name__)` initializes the Flask application.
3. **Define Route for '/' (Default):**
   -  `@app.route('/')` defines a route for the root URL (http://your-server/), which is accessed when no specific path is given.
   -  `def hello_world():` defines the function that handles requests to the root URL.
   -  `return 'Hello World!'` sends back the text "Hello World!" as the response.
4. **Define Route for '/what':**
   -  `@app.route('/what')` defines a new route for the URL `http://your-server/what`.
   -  `def what_do_you_need():` defines the function that handles requests to this route.
   -  `return "I need your instructions to complete the task!"` sends back the specified message.
5. **Run the Application:**
   -  `if __name__ == '__main__':` ensures the code below only runs when the script is executed directly (not imported as a module).
   -  `app.run()` starts the Flask development server, listening for incoming requests.

Now, when you run this modified `hello.py` file and access the URL `http://127.0.0.1:5000/what` in your web browser, you'll see the message "I need your instructions to complete the task!".
