from ..models import OdczytPogody
from ..services.validation import validate_temperatura, validate_ciagnienie
from ..database.memory_db import MemoryDB

class WeatherController:
    def __init__(self):
        self.db = MemoryDB()

    def get_weather(self, timestamp):
        data = self.db.get_data(timestamp)
        validate_temperatura(data.temperatura)
        validate_ciagnienie(data.ciagnienie)
        return data.__dict__