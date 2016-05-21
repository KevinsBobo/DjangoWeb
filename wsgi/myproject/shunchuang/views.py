#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from shunchuang.models import Person

# Create your views here.

def index(request):
    name = Person.objects.get(name="KevinsBobo")
    return render(request, 'shunchuang/index.html', {'name': name.name, 'age': name.age})

def user_isexist(request):
    pass

def phone_isexist(request):
    pass

def email_isexist(request):
    pass

def creat_user(request):
    pass
