import requests
from urllib.parse import quote
from app.config.settings import WEATHER_API

class WeatherService:

    def get_weather(self, city: str):

        url = f"{WEATHER_API.rstrip('/')}/{quote(city)}"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()
            current = data["current"]

            return {
                "city": city,
                "temperature": current["temperature_2m"],
                "humidity": current["relative_humidity_2m"],
                "wind_speed": current["wind_speed_10m"],
            }

        except requests.HTTPError as e:
            raise Exception(f"Erro ao consultar a cidade '{city}': {e}")

        except requests.RequestException as e:
            raise Exception(f"Não foi possível conectar à API de clima: {e}")