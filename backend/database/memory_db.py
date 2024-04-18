class MemoryDB:
    def __init__(self):
        self.data = {}

    def get_data(self, timestamp):
        return self.data.get(timestamp)

    def add_data(self, data):
        self.data[data.timestamp] = data