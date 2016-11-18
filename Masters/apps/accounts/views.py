from django.shortcuts import render, redirect
from models import User
from landing.views import LandingView
from django.http import JsonResponse
import re

def isEmailValid(email):
    return bool(re.fullmatch("[A-Za-z\.0-9]+@[A-Za-z0-9]+\.[A-Za-z]+", email))

def isDormitoryValid(dorm):
    try:
        v = int(dorm)
        return v <= 10 and v > 0
    except ValueError:
        return False

def isRoomValid(room):
    try:
        v = int(room)
        return v < 1000 and v > 0
    except ValueError:
        return False

def registrationView(request):
    if request.method == 'GET':
        return render(request, "templates/registration.html")
    else:
        if (User.objects.filter(email=request.POST['email']).count() > 0 or not
        isEmailValid(request.POST['email']) or not isDormitoryValid(request.POST['email']) or not isRoomValid(request.POST['email'])):
            return JsonResponse({'status': 'failed'})
        User(request.POST).save()
        return loginView(request)
