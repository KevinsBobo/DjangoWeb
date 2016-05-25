# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from shunchuang.models import Person
from shunchuang.models import UserProfile
from shunchuang.forms  import LoginForm

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
            return render(request, 'shunchuang/my.html', {'active_my': 'active', 'form': form, 'user': False})
            if result:
                return HttpResponseRedirect('/my/')
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

    def check_verif_post(self, request):
            name = request.POST['username']
            isexist = self.user_isexist(name)
            if isexist:
                return HttpResponse('return1: %s'%(isexist))
            phone = request.POST['phone']
            isexist = self.phone_isexist(phone)
            if isexist:
                return HttpResponse('return2: %s'%(isexist))
            email = request.POST['email']
            isexist = self.email_isexist(email)
            if isexist:
                return HttpResponse('return3: %s'%(isexist))
            return False

    def check_verif(self, request):
        verif = request.GET['verif']
        if verif == '0':
            if not request.POST:
                return render(request, 'registration/sign.html')
            isexist = self.check_verif_post(request)
            return isexist
        else:
            isexist = self.check_verif_get(request)
            return HttpResponse('return: %s'%(isexist))

    def create_user(self, request):

        try:
            if not request.GET:
                return render(request, 'registration/sign.html')
            verif = request.GET['verif']
        except KeyError:
            return render(request, 'registration/sign.html')

        isexist = self.check_verif(request)
        if isexist:
            return isexist

        username = request.POST['username']
        password = request.POST['password']
        phone    = request.POST['phone']
        email    = request.POST['email']
        select   = request.POST['select']
        newuser = User.objects.create_user(
                username = username,
                email    = email,
                password = password)
        newuserprofile = UserProfile(
                username = username,
                email    = email,
                phone    = phone,
                select   = select)
        newuser.save()
        newuserprofile.save()
        return HttpResponse('return: OK')

