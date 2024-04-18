from flask import Flask, request, jsonify
from ..controllers.weather_controller import WeatherController

app = Flask(__name__)
weather_controller = WeatherController()

@app.route('/weather', methods=['GET'])
def get_weather():
    timestamp = request.args.get('timestamp')
    try:
        data = weather_controller.get_weather(timestamp)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400