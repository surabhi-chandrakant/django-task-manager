# weather/services.py
import requests
from django.conf import settings
from django.core.cache import cache

class WeatherService:
    BASE_URL = "https://api.openweathermap.org/data/2.5"
    
    @classmethod
    def get_weather(cls, city):
        cache_key = f"weather_{city.lower()}"
        cached_data = cache.get(cache_key)
        
        if cached_data:
            return cached_data
        
        try:
            response = requests.get(
                f"{cls.BASE_URL}/weather",
                params={
                    'q': city,
                    'appid': settings.WEATHER_API_KEY,
                    'units': 'metric'
                },
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': data['name'],
                    'country': data['sys']['country'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'humidity': data['main']['humidity'],
                    'pressure': data['main']['pressure'],
                    'wind_speed': data['wind']['speed'],
                    'icon': data['weather'][0]['icon']
                }
                
                # Cache for 30 minutes
                cache.set(cache_key, weather_data, 1800)
                return weather_data
            else:
                return {'error': 'City not found'}
                
        except requests.RequestException:
            return {'error': 'Weather service unavailable'}
    
    @classmethod
    def get_forecast(cls, city, days=5):
        try:
            response = requests.get(
                f"{cls.BASE_URL}/forecast",
                params={
                    'q': city,
                    'appid': settings.WEATHER_API_KEY,
                    'units': 'metric',
                    'cnt': days * 8  # 8 forecasts per day (every 3 hours)
                },
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {'error': 'Forecast data not available'}
                
        except requests.RequestException:
            return {'error': 'Weather service unavailable'}