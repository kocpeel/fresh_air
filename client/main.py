from api_client import AirQualityClient

def main():
    client = AirQualityClient()
    data = client.get_air_quality_data("Warszawa")
    print(data)

if __name__ == "__main__":
    main()