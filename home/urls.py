from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rules/', views.rules, name='rules'),
    path('play/', views.play, name='play'),
]
