from flask import Flask, jsonify
from services import fetch_air_quality_data

app = Flask(__name__)

@app.route('/air_quality/<city_name>/<country_name>', methods=['GET'])
def get_air_quality(city_name, country_name):
    data = fetch_air_quality_data(city_name, country_name)
    return jsonify(data)