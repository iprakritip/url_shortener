from django.urls import path
from shortener.views import shortener

urlpatterns = [
    path('', shortener, name='shortener')
]