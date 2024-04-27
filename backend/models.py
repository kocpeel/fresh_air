class AirQualityData:
    def __init__(self, timestamp, aqius, aqicn, temperature, pressure, humidity, wind_speed, wind_direction, pollutants):
        self.timestamp = timestamp
        self.aqius = aqius
        self.aqicn = aqicn
        self.temperature = self.validate_temperature(temperature)
        self.pressure = self.validate_pressure(pressure)
        self.humidity = self.validate_humidity(humidity)
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction
        self.pollutants = pollutants

    @staticmethod
    def validate_temperature(temperature):
   
        if not (-50 <= temperature <= 50):
            raise ValueError("Temperatura poza zakresem od -50 do 50 stopni Celsjusza")
        return temperature

    @staticmethod
    def validate_pressure(pressure):
       
        if not (800 <= pressure <= 1200):
            raise ValueError("Ciśnienie poza zakresem od 800 do 1200 hPa")
        return pressure

    @staticmethod
    def validate_humidity(humidity):
      
        if not (0 <= humidity <= 100):
            raise ValueError("Wilgotność poza zakresem od 0 do 100%")
        return humidity