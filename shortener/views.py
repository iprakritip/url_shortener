import json
from shortener.short import add_url
from django.shortcuts import render
from django.http import JsonResponse
from shortener.models import URL_Table
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


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
        user_id=body["user_id"]

        try:
            user = User.objects.get(id=user_id) 
            add_url(original_url,user)
            print(original_url)
            return JsonResponse({"link-status":"received"},status=200)

        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)


@csrf_exempt 
def redirect(request, url):
    try:
        curr_object = URL_Table.objects.get(shortened_url=url)
        curr_object.count+=1
        curr_object.save()
        return JsonResponse({"url": curr_object.original_url})
    except URL_Table.DoesNotExist:
        return JsonResponse({"message": "Page not found."})
