from django.urls import path
from shortener.views import shortener,redirect

urlpatterns = [
    path('', shortener, name='shortener'),
    path('<str:url>', redirect, name='redirect')
]