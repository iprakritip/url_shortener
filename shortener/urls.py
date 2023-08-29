from django.urls import path
from shortener.views import home

urlpatterns = [
    path('home', home, name='home')
]