# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from shunchuang.models import Person
from shunchuang.models import UserProfile
from shunchuang.forms  import LoginForm
from shunchuang.forms  import SignForm

class Index():
    def index(self, request):
        login = Login()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            result = login.loginfun(request, form)
            if result:
                return HttpResponseRedirect('/')
            return render(request, 'shunchuang/index.html', {'active_index': 'active', 'form': form, 'user': False})
        loginform = LoginForm()
        name = login.islogined(request)
        return render(request, 'shunchuang/index.html', {'active_index': 'active', 'form': loginform, 'user': name})

class Search():
    def search(self, request):
        login = Login()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            result = login.loginfun(request, form)
            if result:
                return HttpResponseRedirect('/search/')
            return render(request, 'shunchuang/search.html', {'active_search': 'active', 'form': form, 'user': False})
        name = login.islogined(request)
        loginform = LoginForm()
        return render(request, 'shunchuang/search.html', {'active_search': 'active', 'form': loginform, 'user': name})

class ClassPage():
    def classpage(self, request):
        login = Login()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            result = login.loginfun(request, form)
            if result:
                return HttpResponseRedirect('/class/')
            return render(request, 'shunchuang/class.html', {'active_class': 'active', 'form': form, 'user': False})
        name = login.islogined(request)
        loginform = LoginForm()
        return render(request, 'shunchuang/class.html', {'active_class': 'active', 'form': loginform, 'user': name})

class Auction():
    def auction(self, request):
        login = Login()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            result = login.loginfun(request, form)
            if result:
                return HttpResponseRedirect('/auction/')
            return render(request, 'shunchuang/auction.html', {'active_auction': 'active', 'form': form, 'user': False})
        name = login.islogined(request)
        loginform = LoginForm()
        return render(request, 'shunchuang/auction.html', {'active_auction': 'active', 'form': loginform, 'user': name})

class My():
    def my(self, request):
        login = Login()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            result = login.loginfun(request, form)
            if result:
                return HttpResponseRedirect('/my/')
            return render(request, 'shunchuang/my.html', {'active_my': 'active', 'form': form, 'user': False})
        name = login.islogined(request)
        if not name:
            return HttpResponseRedirect('/login/')

        loginform = LoginForm()
        return render(request, 'shunchuang/my.html', {'active_my': 'active', 'form': loginform, 'user': name})

class Login():
    def islogined(self, request):
        user = request.user
        name = False
        if user.is_authenticated():
            username = user.username
            user = UserProfile.objects.get(username = username)
            name = user.name
            if not name: 
                name = username
        return name


    def logout(self,request):
        auth.logout(request)
        return HttpResponseRedirect('/login/')

    def loginfun(self, request, form):
        if form.is_valid():
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            user = UserProfile.objects.get(phone = phone)
            username = user.username
            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
                return True
            else:
                form.add_error('password', '密码错误')
                return False
        else:
            return False

    def login(self, request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            result = self.loginfun(request, form)
            if result:
                return HttpResponseRedirect('/my/')
            return render(request, 'shunchuang/login.html', {'user': False , 'form': form})

        name = self.islogined(request)
        form = LoginForm()
        return render(request, 'shunchuang/login.html', {'user': name , 'form': form})

class SignModel():
    def user_isexist(self, name):
        username = UserProfile.objects.filter(username__iexact=name)
        isexist = username.exists() 
        return isexist

    def phone_isexist(self, phone):
        userphone = UserProfile.objects.filter(phone__iexact=phone)
        isexist = userphone.exists() 
        return isexist

    def email_isexist(self, email):
        useremail = UserProfile.objects.filter(email__iexact=email)
        isexist = useremail.exists() 
        return isexist

    def check_verif_get(self, request):
        verif = request.GET['verif']
        if verif == '1':
            name = request.GET['username']
            isexist = self.user_isexist(name)
            return isexist
        elif verif == '2':
            phone = request.GET['phone']
            isexist = self.phone_isexist(phone)
            return isexist
        elif verif == '3':
            email = request.GET['email']
            isexist = self.email_isexist(email)
            return isexist
        else:
            isexist = True
            return isexist

    def create_user(self, request):
        signform = SignForm()
        if request.method == 'GET':
            try:    
                verif = request.GET['verif']
                isexist = self.check_verif_get(request)
                return HttpResponse(isexist)
            except KeyError:
                return render(request, 'shunchuang/sign.html', {'signform': signform, 'hidden': 'visibility:hidden'})

        if request.method == 'POST':
            signform = SignForm(request.POST)
            if signform.is_valid():
                newuser = User.objects.create_user(
                        username = signform.cleaned_data['username'],
                        email    = signform.cleaned_data['email'],
                        password = signform.cleaned_data['passwordt'],)
                newuserprofile = UserProfile(
                        username = signform.cleaned_data['username'],
                        email    = signform.cleaned_data['email'],
                        phone    = signform.cleaned_data['phone'],
                        select   = signform.cleaned_data['select'],)
                newuser.save()
                newuserprofile.save()

                username = signform.cleaned_data['username']
                password = signform.cleaned_data['passwordt']
                user = auth.authenticate(username=username, password=password)
                if user is not None and user.is_active:
                    auth.login(request, user)
                return HttpResponseRedirect('/my/')
            return render(request, 'shunchuang/sign.html', {'signform': signform, 'hidden': 'visibility:hidden'})

