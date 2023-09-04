import json 
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from http import HTTPStatus



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
            # print(user.password)
            return JsonResponse({"message":"user registered!!"}, status=HTTPStatus.OK)
        else:
            return JsonResponse({"message":"error registering a new user."}, status=HTTPStatus.BAD_REQUEST)


@csrf_exempt 
def login(request):

    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        username=body["username"]
        password=body["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            
            # print("Welcome to url shortener!!")
            token, created = Token.objects.get_or_create(user=user)  
            if created:
                return JsonResponse({"token": token.key}, status=HTTPStatus.OK)  
            else:
                return JsonResponse({"token": token.key}, status=HTTPStatus.OK)
            
        else:
            # print("Can't log in. Please try again later!")
            return JsonResponse({"message":"login failed"},status=HTTPStatus.NOT_FOUND)

    
