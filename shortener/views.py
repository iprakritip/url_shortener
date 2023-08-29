from django.shortcuts import render
from shortener.models import URL_Table
from shortener.short import add_url
from django.http import JsonResponse

# Create your views here.

# def home(request):
#     url_table=URL_Table.objects.all()
#     return render(request, 'base.html',{"url_table":url_table})

def home(request):
    return JsonResponse({"name":"Ram"})
