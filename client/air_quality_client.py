import requests
from .config import API_KEY, BASE_URL

class AirQualityClient:
    def __init__(self, city_name, country_name):
        self.city_name = city_name
        self.country_name = country_name

    def get_air_quality_data(self):
        params = {
            "city": self.city_name,
            "country": self.country_name,
            "key": API_KEY
        }
        response = requests.get(BASE_URL, params=params)
        return response.json()