# weather/urls.py
from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('dashboard/', views.weather_dashboard, name='dashboard'),
    path('api/<str:city>/', views.get_weather, name='api_weather'),
    path('api/<str:city>/forecast/', views.get_forecast, name='api_forecast'),
]