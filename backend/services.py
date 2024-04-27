from models import AirQualityData
from client.air_quality_client import AirQualityClient

def fetch_air_quality_data(city_name, country_name):
    client = AirQualityClient(city_name, country_name)
    data = client.get_air_quality_data()
    return data