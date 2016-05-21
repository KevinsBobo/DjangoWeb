#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from shunchuang.models import UserProfile
from shunchuang.models import Person

# Create your views here.

def index(request):
    name = Person.objects.get(name="KevinsBobo")
    return render(request, 'shunchuang/index.html', {'name': name.name, 'age': name.age})

def user_isexist(name):
    username = User.objects.filter(username__iexact=name)
    isexist = username.exists() 
    return isexist

def phone_isexist(phone):
    userphone = UserProfile.objects.filter(phone__iexact=phone)
    isexist = userphone.exists() 
    return isexist

def email_isexist(email):
    useremail = UserProfile.objects.filter(email__iexact=email)
    isexist = useremail.exists() 
    return isexist

def check_verif_get(request):
    verif = request.GET['verif']
    if verif == '1':
        name = request.GET['username']
        isexist = user_isexist(name)
        return isexist

    if verif == '2':
        phone = request.GET['phone']
        isexist = phone_isexist(phone)
        return isexist

    if verif == '3':
        email = request.GET['email']
        isexist = email_isexist(email)
        return isexist

def check_verif_post(request):
        name = request.POST['username']
        isexist = user_isexist(name)
        if isexist:
            return HttpResponse('return1: %s'%(isexist))
        phone = request.POST['phone']
        isexist = phone_isexist(phone)
        if isexist:
            return HttpResponse('return2: %s'%(isexist))
        email = request.POST['email']
        isexist = email_isexist(email)
        if isexist:
            return HttpResponse('return3: %s'%(isexist))
        return False

def check_verif(request):
    verif = request.GET['verif']
    if verif == '0':
        isexist = check_verif_post(request)
        return isexist
    else:
        isexist = check_verif_get(request)
        return HttpResponse('return: %s'%(isexist))

def create_user(request):
    isexist = check_verif(request)
    if isexist:
        return isexist

    return HttpResponse('return: OK')

