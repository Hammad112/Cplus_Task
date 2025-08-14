# Cplus TASK (FastAPI + PostgreSQL + Weather API)

This API allows you to:
- **Sign up users** (store in PostgreSQL table `Cplus`)
- **Log in users**
- **Fetch weather forecast** for a given city using OpenWeather API

---

## 📂 Project Structure

```
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
```

---

## ⚙️ Requirements

- Python 3.9+
- PostgreSQL
- OpenWeather API key

---

## 📦 Installation



2️⃣ **Create a virtual environment**

```bash
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate     # Windows
```

3️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

4️⃣ **Setup config.json**
Edit `config.json`:

```json
{
  "db_user": "postgres",
  "db_password": "H****d",
  "db_host": "localhost",
  "db_port": 5432,
  "db_name": "postgres",
  "weather_api_key": "***********"
}
```

5️⃣ **Optional: Set API key in `.env`**

```
WEATHER_API_KEY=your_openweather_api_key
```
API Fetch Link: https://openweathermap.org/api

6️⃣ **Create PostgreSQL database**

```sql
CREATE DATABASE "postgres";
```

7️⃣ **Run the app**

```bash
uvicorn app.main:app --reload
```

---

## 📄 API Endpoints

---

### 1. **Sign Up**

**POST** `/users/`

#### Request Body

```json
{
  "firstname": "Muhammad",
  "lastname": "Ahmed",
  "phone_number": "03348500674",
  "email": "ahmed@gmail.com",
  "password": "Hammad"
}
```

#### Response Example (Image)

![signup-response](images/sp1.PNG)

#### cURL

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "firstname": "Ali",
  "lastname": "Awan",
  "phone_number": "03155583363",
  "email": "ali@gmail.com",
  "password": "AliAwan"
}'
```

---

### 2. **Login**

**POST** `/login/`

#### Request Body

```json
{
  "email": "ali@gmail.com",
  "password": "AliAwan"
}
```

#### Response Example (Image)

![login-response](images/lg1.PNG)

#### cURL

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/login/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "ali@gmail.com",
  "password": "AliAwan"
}'
```

---

### 3. **Weather Forecast**

**GET** `/weather/{city}`

#### Example Request

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/weather/Karachi' \
  -H 'accept: application/json'
```

#### Response Example 

![weather-response](images/w1.PNG)

---

#### Existing Responsee 
![table-data](images/tbPNG.PNG)


## 🚀 Running Tests

Once server is running:

* Visit Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Try endpoints directly from the browser

---


