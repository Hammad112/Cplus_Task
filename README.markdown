# Cplus API (FastAPI + PostgreSQL + Weather API)

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
  "firstname": "John",
  "lastname": "Doe",
  "phone_number": "9876543210",
  "email": "john@example.com",
  "password": "securepass"
}
```

#### Response Example (Image)

![signup-response](images/signup-response.png)

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
  "email": "john@example.com",
  "password": "securepass"
}
```

#### Response Example (Image)

![login-response](images/lg1.png)

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
```json
{
  "cod": "200",
  "message": 0,
  "cnt": 40,
  "list": [
    {
      "dt": 1755172800,
      "main": {
        "temp": 30.43,
        "feels_like": 34.59,
        "temp_min": 30.43,
        "temp_max": 30.43,
        "pressure": 1000,
        "sea_level": 1000,
        "grnd_level": 996,
        "humidity": 64,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 95
      },
      "wind": {
        "speed": 5.07,
        "deg": 198,
        "gust": 4.59
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2025-08-14 12:00:00"
    },
    {
      "dt": 1755183600,
      "main": {
        "temp": 29.78,
        "feels_like": 34.06,
        "temp_min": 28.49,
        "temp_max": 29.78,
        "pressure": 1000,
        "sea_level": 1000,
        "grnd_level": 997,
        "humidity": 68,
        "temp_kf": 1.29
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 97
      },
      "wind": {
        "speed": 4.64,
        "deg": 208,
        "gust": 5.43
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2025-08-14 15:00:00"
    },
    {
      "dt": 1755194400,
      "main": {
        "temp": 28.82,
        "feels_like": 32.88,
        "temp_min": 28.02,
        "temp_max": 28.82,
        "pressure": 1001,
        "sea_level": 1001,
        "grnd_level": 999,
        "humidity": 73,
        "temp_kf": 0.8
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 98
      },
      "wind": {
        "speed": 2.59,
        "deg": 224,
        "gust": 2.84
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2025-08-14 18:00:00"
    },
    {
      "dt": 1755205200,
      "main": {
        "temp": 27.66,
        "feels_like": 31,
        "temp_min": 27.66,
        "temp_max": 27.66,
        "pressure": 1001,
        "sea_level": 1001,
        "grnd_level": 997,
        "humidity": 78,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 100
      },
      "wind": {
        "speed": 1.97,
        "deg": 206,
        "gust": 2.25
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2025-08-14 21:00:00"
    },
    {
      "dt": 1755216000,
      "main": {
        "temp": 27.55,
        "feels_like": 30.63,
        "temp_min": 27.55,
        "temp_max": 27.55,
        "pressure": 1001,
        "sea_level": 1001,
        "grnd_level": 997,
        "humidity": 77,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 100
      },
      "wind": {
        "speed": 1.77,
        "deg": 206,
        "gust": 1.88
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2025-08-15 00:00:00"
    },
    {
      "dt": 1755226800,
      "main": {
        "temp": 27.8,
        "feels_like": 31.05,
        "temp_min": 27.8,
        "temp_max": 27.8,
        "pressure": 1002,
        "sea_level": 1002,
        "grnd_level": 999,
        "humidity": 76,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 100
      },
      "wind": {
        "speed": 1.4,
        "deg": 223,
        "gust": 1.19
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2025-08-15 03:00:00"
    },
    {
      "dt": 1755237600,
      "main": {
        "temp": 30.59,
        "feels_like": 34.46,
        "temp_min": 30.59,
        "temp_max": 30.59,
        "pressure": 1002,
        "sea_level": 1002,
        "grnd_level": 999,
        "humidity": 62,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 100
      },
      "wind": {
        "speed": 3.3,
        "deg": 174,
        "gust": 3.17
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2025-08-15 06:00:00"
    },
    {
      "dt": 1755248400,
      "main": {
        "temp": 31.86,
        "feels_like": 35.62,
        "temp_min": 31.86,
        "temp_max": 31.86,
        "pressure": 1001,
        "sea_level": 1001,
        "grnd_level": 997,
        "humidity": 56,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 100
      },
      "wind": {
        "speed": 5.18,
        "deg": 185,
        "gust": 4.19
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2025-08-15 09:00:00"
    },
    {
      "dt": 1755259200,
      "main": {
        "temp": 31.14,
        "feels_like": 34.64,
        "temp_min": 31.14,
        "temp_max": 31.14,
        "pressure": 1000,
        "sea_level": 1000,
        "grnd_level": 996,
        "humidity": 58,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 99
      },
      "wind": {
        "speed": 5.83,
        "deg": 190,
        "gust": 4.97
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2025-08-15 12:00:00"
    },
    {
      "dt": 1755270000,
      "main": {
        "temp": 29.02,
        "feels_like": 32.77,
        "temp_min": 29.02,
        "temp_max": 29.02,
        "pressure": 1001,
        "sea_level": 1001,
        "grnd_level": 997,
        "humidity": 70,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 100
      },
      "wind": {
        "speed": 4.89,
        "deg": 209,
        "gust": 5.42
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2025-08-15 15:00:00"
    },
    {
      "dt": 1755280800,
      "main": {
        "temp": 28.6,
        "feels_like": 32.38,
        "temp_min": 28.6,
        "temp_max": 28.6,
        "pressure": 1001,
        "sea_level": 1001,
        "grnd_level": 998,
        "humidity": 73,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 100
      },
      "wind": {
        "speed": 3.61,
        "deg": 222,
        "gust": 4.27
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2025-08-15 18:00:00"
    },
    {
      "dt": 1755291600,
      "main": {
        "temp": 28.07,
        "feels_like": 31.36,
        "temp_min": 28.07,
        "temp_max": 28.07,
        "pressure": 1000,
        "sea_level": 1000,
        "grnd_level": 997,
        "humidity": 74,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03n"
        }
      ],
      "clouds": {
        "all": 40
      },
      "wind": {
        "speed": 2.78,
        "deg": 234,
        "gust": 3.2
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2025-08-15 21:00:00"
    },
    {
      "dt": 1755302400,
      "main": {
        "temp": 27.7,
        "feels_like": 30.83,
        "temp_min": 27.7,
        "temp_max": 27.7,
        "pressure": 1000,
        "sea_level": 1000,
        "grnd_level": 997,
        "humidity": 76,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03n"
        }
      ],
      "clouds": {
        "all": 25
      },
      "wind": {
        "speed": 2.12,
        "deg": 256,
        "gust": 2.47
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2025-08-16 00:00:00"
    },
    {
      "dt": 1755313200,
      "main": {
        "temp": 28.31,
        "feels_like": 31.58,
        "temp_min": 28.31,
        "temp_max": 28.31,
        "pressure": 1001,
        "sea_level": 1001,
        "grnd_level": 998,
        "humidity": 72,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01d"
        }
      ],
      "clouds": {
        "all": 4
      },
      "wind": {
        "speed": 2.5,
        "deg": 243,
        "gust": 2.7
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2025-08-16 03:00:00"
    },
    {
      "dt": 1755324000,
      "main": {
        "temp": 31.4,
        "feels_like": 35.18,
        "temp_min": 31.4,
        "temp_max": 31.4,
        "pressure": 1001,
        "sea_level": 1001,
        "grnd_level": 998,
        "humidity": 58,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01d"
        }
      ],
      "clouds": {
        "all": 6
      },
      "wind": {
        "speed": 3.5,
        "deg": 211,
        "gust": 2.78
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2025-08-16 06:00:00"
    },
    {
      "dt": 1755334800,
      "main": {
        "temp": 33,
        "feels_like": 36.88,
        "temp_min": 33,
        "temp_max": 33,
        "pressure": 999,
        "sea_level": 999,
        "grnd_level": 996,
        "humidity": 52,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02d"
        }
      ],
      "clouds": {
        "all": 13
      },
      "wind": {
        "speed": 6.22,
        "deg": 199,
        "gust": 4.16
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2025-08-16 09:00:00"
    },
    {
      "dt": 1755345600,
      "main": {
        "temp": 31.43,
        "feels_like": 34.99,
        "temp_min": 31.43,
        "temp_max": 31.43,
        "pressure": 999,
        "sea_level": 999,
        "grnd_level": 995,
        "humidity": 57,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
        }
      ],
      "clouds": {
        "all": 40
      },
      "wind": {
        "speed": 5.85,
        "deg": 207,
        "gust": 5.07
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2025-08-16 12:00:00"
    },
    {
      "dt": 1755356400,
      "main": {
        "temp": 29.29,
        "feels_like": 32.98,
        "temp_min": 29.29,
        "temp_max": 29.29,
        "pressure": 1000,
        "sea_level": 1000,
        "grnd_level": 997,
        "humidity": 68,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 55
      },
      "wind": {
        "speed": 5.08,
        "deg": 218,
        "gust": 5.59
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2025-08-16 15:00:00"
    },
    {
      "dt": 1755367200,
      "main": {
        "temp": 28.69,
        "feels_like": 32.23,
        "temp_min": 28.69,
        "temp_max": 28.69,
        "pressure": 1001,
        "sea_level": 1001,
        "grnd_level": 998,
        "humidity": 71,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03n"
        }
      ],
      "clouds": {
        "all": 35
      },
      "wind": {
        "speed": 4.37,
        "deg": 242,
        "gust": 4.86
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2025-08-16 18:00:00"
    },
    {
      "dt": 1755378000,
      "main": {
        "temp": 28,
        "feels_like": 31.5,
        "temp_min": 28,
        "temp_max": 28,
        "pressure": 1000,
        "sea_level": 1000,
        "grnd_level": 996,
        "humidity": 76,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02n"
        }
      ],
      "clouds": {
        "all": 16
      },
      "wind": {
        "speed": 4.51,
        "deg": 266,
        "gust": 5.1
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2025-08-16 21:00:00"
    },
    {
      "dt": 1755388800,
      "main": {
        "temp": 27.41,
        "feels_like": 30.67,
        "temp_min": 27.41,
        "temp_max": 27.41,
        "pressure": 1000,
        "sea_level": 1000,
        "grnd_level": 996,
        "humidity": 80,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02n"
        }
      ],
      "clouds": {
        "all": 19
      },
      "wind": {
        "speed": 3.97,
        "deg": 281,
        "gust": 4.69
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2025-08-17 00:00:00"
    },
    {
      "dt": 1755399600,
      "main": {
        "temp": 28.39,
        "feels_like": 31.91,
        "temp_min": 28.39,
        "temp_max": 28.39,
        "pressure": 1001,
        "sea_level": 1001,
        "grnd_level": 997,
        "humidity": 73,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 66
      },
      "wind": {
        "speed": 3.66,
        "deg": 264,
        "gust": 4.01
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2025-08-17 03:00:00"
    },
    {
      "dt": 1755410400,
      "main": {
        "temp": 31.67,
        "feels_like": 35.76,
        "temp_min": 31.67,
        "temp_max": 31.67,
        "pressure": 1001,
        "sea_level": 1001,
        "grnd_level": 997,
        "humidity": 58,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
        }
      ],
      "clouds": {
        "all": 43
      },
      "wind": {
        "speed": 4.84,
        "deg": 213,
        "gust": 4.11
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2025-08-17 06:00:00"
    },
    {
      "dt": 1755421200,
      "main": {
        "temp": 32.6,
        "feels_like": 37.23,
        "temp_min": 32.6,
        "temp_max": 32.6,
        "pressure": 999,
        "sea_level": 999,
        "grnd_level": 996,
        "humidity": 56,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 70
      },
      "wind": {
        "speed": 6.24,
        "deg": 216,
        "gust": 4.96
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2025-08-17 09:00:00"
    },
    {
      "dt": 1755432000,
      "main": {
        "temp": 31.07,
        "feels_like": 35.51,
        "temp_min": 31.07,
        "temp_max": 31.07,
        "pressure": 999,
        "sea_level": 999,
        "grnd_level": 996,
        "humidity": 62,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 83
      },
      "wind": {
        "speed": 6.13,
        "deg": 210,
        "gust": 5.5
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2025-08-17 12:00:00"
    },
    {
      "dt": 1755442800,
      "main": {
        "temp": 28.75,
        "feels_like": 32.72,
        "temp_min": 28.75,
        "temp_max": 28.75,
        "pressure": 1001,
        "sea_level": 1001,
        "grnd_level": 997,
        "humidity": 73,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 99
      },
      "wind": {
        "speed": 5.24,
        "deg": 218,
        "gust": 5.84
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2025-08-17 15:00:00"
    },
    {
      "dt": 1755453600,
      "main": {
        "temp": 28.49,
        "feels_like": 32.47,
        "temp_min": 28.49,
        "temp_max": 28.49,
        "pressure": 1002,
        "sea_level": 1002,
        "grnd_level": 998,
        "humidity": 75,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 100
      },
      "wind": {
        "speed": 4.48,
        "deg": 259,
        "gust": 5.1
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2025-08-17 18:00:00"
    },
    {
      "dt": 1755464400,
      "main": {
        "temp": 27.7,
        "feels_like": 31.23,
        "temp_min": 27.7,
        "temp_max": 27.7,
        "pressure": 1001,
        "sea_level": 1001,
        "grnd_level": 997,
        "humidity": 79,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 77
      },
      "wind": {
        "speed": 4.74,
        "deg": 271,
        "gust": 5.5
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2025-08-17 21:00:00"
    },
    {
      "dt": 1755475200,
      "main": {
        "temp": 27.25,
        "feels_like": 30.52,
        "temp_min": 27.25,
        "temp_max": 27.25,
        "pressure": 1001,
        "sea_level": 1001,
        "grnd_level": 997,
        "humidity": 82,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 64
      },
      "wind": {
        "speed": 4.25,
        "deg": 266,
        "gust": 5.4
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2025-08-18 00:00:00"
    },
    {
      "dt": 1755486000,
      "main": {
        "temp": 28.28,
        "feels_like": 31.98,
        "temp_min": 28.28,
        "temp_max": 28.28,
        "pressure": 1002,
        "sea_level": 1002,
        "grnd_level": 998,
        "humidity": 75,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01d"
        }
      ],
      "clouds": {
        "all": 0
      },
      "wind": {
        "speed": 4.22,
        "deg": 247,
        "gust": 4.96
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2025-08-18 03:00:00"
    },
    {
      "dt": 1755496800,
      "main": {
        "temp": 31.34,
        "feels_like": 36.12,
        "temp_min": 31.34,
        "temp_max": 31.34,
        "pressure": 1002,
        "sea_level": 1002,
        "grnd_level": 998,
        "humidity": 62,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01d"
        }
      ],
      "clouds": {
        "all": 5
      },
      "wind": {
        "speed": 6.24,
        "deg": 240,
        "gust": 6.05
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2025-08-18 06:00:00"
    },
    {
      "dt": 1755507600,
      "main": {
        "temp": 32.16,
        "feels_like": 37.14,
        "temp_min": 32.16,
        "temp_max": 32.16,
        "pressure": 1000,
        "sea_level": 1000,
        "grnd_level": 997,
        "humidity": 59,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
        }
      ],
      "clouds": {
        "all": 33
      },
      "wind": {
        "speed": 6.99,
        "deg": 236,
        "gust": 6.39
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2025-08-18 09:00:00"
    },
    {
      "dt": 1755518400,
      "main": {
        "temp": 30.57,
        "feels_like": 35.15,
        "temp_min": 30.57,
        "temp_max": 30.57,
        "pressure": 1000,
        "sea_level": 1000,
        "grnd_level": 996,
        "humidity": 65,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
        }
      ],
      "clouds": {
        "all": 49
      },
      "wind": {
        "speed": 6.21,
        "deg": 234,
        "gust": 6.17
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2025-08-18 12:00:00"
    },
    {
      "dt": 1755529200,
      "main": {
        "temp": 28.52,
        "feels_like": 32.54,
        "temp_min": 28.52,
        "temp_max": 28.52,
        "pressure": 1001,
        "sea_level": 1001,
        "grnd_level": 997,
        "humidity": 75,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02n"
        }
      ],
      "clouds": {
        "all": 21
      },
      "wind": {
        "speed": 5.87,
        "deg": 238,
        "gust": 6.78
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2025-08-18 15:00:00"
    },
    {
      "dt": 1755540000,
      "main": {
        "temp": 27.89,
        "feels_like": 31.68,
        "temp_min": 27.89,
        "temp_max": 27.89,
        "pressure": 1002,
        "sea_level": 1002,
        "grnd_level": 998,
        "humidity": 79,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03n"
        }
      ],
      "clouds": {
        "all": 48
      },
      "wind": {
        "speed": 5.53,
        "deg": 251,
        "gust": 6.66
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2025-08-18 18:00:00"
    },
    {
      "dt": 1755550800,
      "main": {
        "temp": 27.3,
        "feels_like": 30.64,
        "temp_min": 27.3,
        "temp_max": 27.3,
        "pressure": 1001,
        "sea_level": 1001,
        "grnd_level": 997,
        "humidity": 82,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03n"
        }
      ],
      "clouds": {
        "all": 47
      },
      "wind": {
        "speed": 5.56,
        "deg": 253,
        "gust": 6.96
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2025-08-18 21:00:00"
    },
    {
      "dt": 1755561600,
      "main": {
        "temp": 27.42,
        "feels_like": 30.7,
        "temp_min": 27.42,
        "temp_max": 27.42,
        "pressure": 1000,
        "sea_level": 1000,
        "grnd_level": 997,
        "humidity": 80,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 57
      },
      "wind": {
        "speed": 5.98,
        "deg": 257,
        "gust": 7.52
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2025-08-19 00:00:00"
    },
    {
      "dt": 1755572400,
      "main": {
        "temp": 28.45,
        "feels_like": 32.21,
        "temp_min": 28.45,
        "temp_max": 28.45,
        "pressure": 1001,
        "sea_level": 1001,
        "grnd_level": 998,
        "humidity": 74,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 100
      },
      "wind": {
        "speed": 5.64,
        "deg": 252,
        "gust": 6.73
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2025-08-19 03:00:00"
    },
    {
      "dt": 1755583200,
      "main": {
        "temp": 31.23,
        "feels_like": 35.87,
        "temp_min": 31.23,
        "temp_max": 31.23,
        "pressure": 1000,
        "sea_level": 1000,
        "grnd_level": 997,
        "humidity": 62,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 72
      },
      "wind": {
        "speed": 6.65,
        "deg": 257,
        "gust": 6.28
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2025-08-19 06:00:00"
    },
    {
      "dt": 1755594000,
      "main": {
        "temp": 30.56,
        "feels_like": 35.13,
        "temp_min": 30.56,
        "temp_max": 30.56,
        "pressure": 999,
        "sea_level": 999,
        "grnd_level": 995,
        "humidity": 65,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 89
      },
      "wind": {
        "speed": 6.48,
        "deg": 260,
        "gust": 6.08
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2025-08-19 09:00:00"
    }
  ],
  "city": {
    "id": 1174872,
    "name": "Karachi",
    "coord": {
      "lat": 24.9056,
      "lon": 67.0822
    },
    "country": "PK",
    "population": 11624219,
    "timezone": 18000,
    "sunrise": 1755133522,
    "sunset": 1755180457
  }
}
```

![weather-response](images/weather-response.png)

---



## 🚀 Running Tests

Once server is running:

* Visit Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Try endpoints directly from the browser

---


