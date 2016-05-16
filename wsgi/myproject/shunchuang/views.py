#coding:utf-8
from django.shortcuts import render
from django.http import HeepResponse

# Create your views here.

def index(request):
    return HeepResponse(u"shunchuang!")
