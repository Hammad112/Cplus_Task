Cplus API (FastAPI + PostgreSQL + Weather API)
This API allows you to:

Sign up users (store in PostgreSQL table Cplus)
Log in users
Fetch weather forecast for a given city using OpenWeather API


📂 Project Structure
Cplus_Task/
│── app/
│   │── __init__.py
│   │── database.py
│   │── main.py
│   │── models.py
│   │── schemas.py
│   │── weather.py
│── config.json
│── .env
│── requirements.txt
│── README.md
│── images/
│    │── signup-response.png
│    │── login-response.png
│    │── weather-response.png


⚙️ Requirements

Python 3.9+
PostgreSQL
OpenWeather API key


📦 Installation
1️⃣ Clone the repository
git clone https://github.com/<your-username>/Cplus_Task.git
cd Cplus_Task

2️⃣ Create a virtual environment
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate     # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Setup config.jsonEdit config.json:
{
  "db_user": "postgres",
  "db_password": "yourpassword",
  "db_host": "localhost",
  "db_port": 5432,
  "db_name": "Cplus",
  "weather_api_key": "your_default_api_key"
}

5️⃣ Optional: Set API key in .env
WEATHER_API_KEY=your_openweather_api_key

6️⃣ Create PostgreSQL database
CREATE DATABASE "Cplus";

7️⃣ Run the app
uvicorn app.main:app --reload


📄 API Endpoints

1. Sign Up
POST /users/
Request Body
{
  "firstname": "John",
  "lastname": "Doe",
  "phone_number": "9876543210",
  "email": "john@example.com",
  "password": "securepass"
}

Response Example (Image)

cURL
curl -X POST "http://127.0.0.1:8000/users/" \
-H "Content-Type: application/json" \
-d '{"firstname":"John","lastname":"Doe","phone_number":"9876543210","email":"john@example.com","password":"securepass"}'


2. Login
POST /login/
Request Body
{
  "email": "john@example.com",
  "password": "securepass"
}

Response Example (Image)

cURL
curl -X POST "http://127.0.0.1:8000/login/" \
-H "Content-Type: application/json" \
-d '{"email":"john@example.com","password":"securepass"}'


3. Weather Forecast
GET /weather/{city}
Example Request
curl -X GET "http://127.0.0.1:8000/weather/London"

Response Example (Image)



🚀 Running Tests
Once server is running:

Visit Swagger UI: http://127.0.0.1:8000/docs
Try endpoints directly from the browser


📌 Notes

Passwords are currently stored in plain text — not secure for production.
For production, implement password hashing (bcrypt) and JWT authentication.
