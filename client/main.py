from air_quality_client import AirQualityClient

if __name__ == "__main__":
    client = AirQualityClient("Warszawa", "Poland")
    data = client.get_air_quality_data()
    print(data)