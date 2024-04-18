from flask import Flask
from views.weather_view import app as weather_app

def create_app():
    app = Flask(__name__)
    app.register_blueprint(weather_app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=5000) # Zgodnie z konfiguracją w backend/config.py