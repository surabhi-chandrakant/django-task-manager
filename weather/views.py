# weather/views.py
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .services import WeatherService

@api_view(['GET'])
def get_weather(request, city):
    weather_data = WeatherService.get_weather(city)
    return Response(weather_data)

@api_view(['GET'])
def get_forecast(request, city):
    days = request.GET.get('days', 5)
    try:
        days = int(days)
        if days > 5:
            days = 5
    except ValueError:
        days = 5
    
    forecast_data = WeatherService.get_forecast(city, days)
    return Response(forecast_data)

def weather_dashboard(request):
    return render(request, 'weather/weather_dashboard.html')