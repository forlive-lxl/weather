from flask import Blueprint, jsonify, request
from utils.weather_api import get_weather_by_city
from utils.exceptions import handle_weather_api_exceptions

api_bp = Blueprint('api', __name__)

@api_bp.route('/weather', methods=['GET'])
@handle_weather_api_exceptions
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    weather_data = get_weather_by_city(city)
    return jsonify(weather_data)