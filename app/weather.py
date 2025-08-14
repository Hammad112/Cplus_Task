import os
import json
import requests
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Load config.json
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config.json")
if not os.path.exists(CONFIG_PATH):
    raise FileNotFoundError(f"Config file not found: {CONFIG_PATH}")

with open(CONFIG_PATH) as f:
    config = json.load(f)

# Use .env key if available
API_KEY = os.getenv("WEATHER_API_KEY", config.get("weather_api_key"))
if not API_KEY:
    raise ValueError("Weather API key missing in config.json or .env")

def get_weather_forecast(city: str):
    url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Weather API error: {response.status_code} - {response.text}")
    return response.json()
