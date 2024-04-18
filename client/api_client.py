import requests
from .config import API_URL, API_KEY

class AirQualityClient:
    def get_air_quality_data(self, city):
        response = requests.get(f"{API_URL}/v2/city?city={city}&key={API_KEY}")
        return response.json()