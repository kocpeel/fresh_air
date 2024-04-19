import requests
from config import API_URL, API_KEY
# API_URL = "http://api.airvisual.com/v2/"
# API_KEY = "18b34ba2-c1fb-4892-b559-1b4e492ef7b6"

class AirQualityClient:
    def get_air_quality_data(self, city):
        response = requests.get(f"{API_URL}/city?city={city}&key={API_KEY}")
        # response = requests.get("http://api.airvisual.com/v2/city?city=Warszawa&key=18b34ba2-c1fb-4892-b559-1b4e492ef7b6")
     #   curl --location -g 'http://api.airvisual.com/v2/nearest_station?key={{YOUR_API_KEY}}'
        

        return response.json()