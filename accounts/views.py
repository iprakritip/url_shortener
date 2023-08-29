import json 
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User



# Create your views here.
@csrf_exempt 
def register(request):

    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        username=body["username"]
        email=body["email"]
        password=body["password"]

        if username and email  and password:
            user=User.objects.create_user(username, email, password)
            print(user.password)
            return JsonResponse({"message":"user registered!!"})
        else:
            return JsonResponse({"message":"error registering a new user."})

        
