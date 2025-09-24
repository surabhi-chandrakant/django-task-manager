# tasks/urls.py
from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
]