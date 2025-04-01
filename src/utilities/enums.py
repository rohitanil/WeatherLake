from enum import Enum


class CONSTANTS(Enum):
    WEATHER_API = "https://api.weatherapi.com/v1/current.json"
    STATES = ["San Francisco", "New York", "Los Angeles"]
    AQI_FLAG = "yes"
    KAFKA_TOPIC = "weather"
    INTERVAL = 10
    BOOTSTRAP_SERVER = "localhost:9092"


class KAFKA_CONFIGURATION_CONSTANTS(Enum):
    RETRIES = 5  # Increase retries
    LINGER_MS = 500  # Increase linger time for batch formation
    REQ_TIMEOUT_MS = 60000  # Increase request timeout
    MAX_BLOCK_MS = 60000
    ENCODING = 'utf-8'
