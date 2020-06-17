from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.questions, name='questions'),
    # path('<str:questions_id>/', views.details, name='details')
]
