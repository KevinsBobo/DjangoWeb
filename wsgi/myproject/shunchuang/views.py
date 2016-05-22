#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from shunchuang.models import UserProfile
from shunchuang.models import Person
from shunchuang.kevins import SignModel

# Create your views here.

def index(request):
    name = Person.objects.get(name="KevinsBobo")
    return render(request, 'shunchuang/index.html', {'active_home': 'active','name': name.name, 'age': name.age})

def create_user(request):
    sign = SignModel()
    result = sign.create_user(request)
    return result

