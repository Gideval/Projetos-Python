from langchain.tools import tool
from app.services.weather_service import WeatherService

weather_service = WeatherService()

@tool
def get_weather(city: str) -> str:
    """
    Obtém os dados atuais do clima de uma cidade.

    Utilize esta ferramenta sempre que o usuário perguntar
    sobre temperatura, clima, vento ou umidade.
    """
    weather = weather_service.get_weather(city)

    return f"""
Cidade: {weather["city"]}
Temperatura: {weather["temperature"]} °C
Umidade: {weather["humidity"]} %
Velocidade do vento: {weather["wind_speed"]} km/h
"""