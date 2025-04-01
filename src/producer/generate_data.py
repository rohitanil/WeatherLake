import requests
import os
from src.utilities.enums import CONSTANTS


def get_weather():
    url = CONSTANTS.WEATHER_API.value
    states = CONSTANTS.STATES.value
    aqi_flag = CONSTANTS.AQI_FLAG.value
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        print("Error: API key not found. Set the WEATHER_API_KEY environment variable.")
        return

    batch = {}
    try:
        for state in states:
            params = {
                "key": api_key,
                "q": state,
                "aqi": aqi_flag
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            batch[state] = response.json()
        return batch
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

