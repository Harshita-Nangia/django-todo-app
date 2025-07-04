from django.urls import path
from app_todolist import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
]