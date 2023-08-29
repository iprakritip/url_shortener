import json
from shortener.short import add_url
from django.shortcuts import render
from django.http import JsonResponse
from shortener.models import URL_Table
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


# def home(request):
#     url_table=URL_Table.objects.all()
#     return render(request, 'base.html',{"url_table":url_table})

@csrf_exempt 
def shortener(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        original_url=body["original_url"]
        add_url(original_url)
        print(original_url)
    return JsonResponse({"link-status":"received"})
