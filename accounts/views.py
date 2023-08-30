import json 
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt



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
            return JsonResponse({"message":"user registered!!"}, status=200)
        else:
            return JsonResponse({"message":"error registering a new user."}, status=400)


@csrf_exempt 
def login(request):

    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        username=body["username"]
        password=body["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            
            print("Welcome to url shortener!!")
            token, created = Token.objects.get_or_create(user=user)  # Get or create token
            if created:
                return JsonResponse({"token": token.key}, status=200)  # Return the token
            else:
                return JsonResponse({"token": token.key}, status=200)
            
        else:
            print("Can't log in. Please try again later!")
            return JsonResponse({"message":"login failed"},status=404)

    
