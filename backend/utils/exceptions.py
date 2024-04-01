from functools import wraps
from flask import jsonify

class WeatherAPIException(Exception):
    def __init__(self, message, status_code=500):
        super().__init__(self)
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        return {'error': self.message}

def handle_weather_api_exceptions(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except WeatherAPIException as e:
            response = jsonify(e.to_dict())
            response.status_code = e.status_code
            return response
    return decorated_function
