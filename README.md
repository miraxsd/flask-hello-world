# Prayer Times API

## Project Description
The Prayer Times API is a Flask-based web service designed to provide users with accurate daily prayer times based on their geographical location. The main goals of this project are to facilitate easy access to prayer times for Muslims around the world and to serve as a foundation for further enhancements related to Islamic practices.

### Key Features
- **Dynamic Prayer Time Retrieval**: Get prayer times based on a specified location and date.
- **JSON Response**: Receive data in a structured JSON format for easy integration into applications.
- **Date Flexibility**: Support for retrieving prayer times for any specified date.
- **Lunativ Endpoint**: New endpoint to provide prayer times based on lunar calendar dates.

### Target Audience
This project is aimed at developers building applications or services for the Muslim community that requires access to prayer times, as well as individuals interested in integrating prayer time features into their own applications.

### Prerequisites
- Python 3.x
- Flask
- Requests library (if further extensions are planned)

## Installation Instructions
To install the necessary dependencies and run the project, follow these steps:

1. Clone the repository:
   git clone https://github.com/yourusername/prayer-times-api.git
   cd prayer-times-api

2. Create a virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
   pip install Flask requests

## Usage Examples
To start the API, run the following command in your terminal:
python app.py
Once the server is running, you can access the prayer times by sending a GET request to the following endpoints:
- For standard prayer times:
  http://127.0.0.1:5000/api/prayer-times?location=YourLocation&date=YYYY-MM-DD
  For example:
  http://127.0.0.1:5000/api/prayer-times?location=NewYork&date=2023-10-01

- For lunar calendar prayer times:
  http://127.0.0.1:5000/api/lunativ?location=YourLocation&lunar_date=YYYY-MM-DD
  For example:
  http://127.0.0.1:5000/api/lunativ?location=NewYork&lunar_date=1445-03-15

## Contribution Guidelines
If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the project's coding standards and is well-documented.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.