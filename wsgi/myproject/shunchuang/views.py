#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from shunchuang.models import Person

# Create your views here.

def index(request):
    name = Person.objects.get(name="KevinsBobo")
    return HttpResponse(name)
