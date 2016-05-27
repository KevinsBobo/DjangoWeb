# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from collections import OrderedDict
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from shunchuang.models import Person
from shunchuang.models import UserProfile
from shunchuang.forms  import LoginForm
from shunchuang.forms  import SignForm
from shunchuang.forms  import EditinfoForm

class Index():
    def index(self, request):
        login = Login()
        loginform = LoginForm()
        name = login.islogined(request)
        if request.method == 'POST':
            form = LoginForm(request.POST)
            result = login.loginfun(request, form)
            if result:
                return HttpResponseRedirect('/')
            return render(request, 'shunchuang/index.html', {'active_index': 'active', 'form': form, 'user': False})
        return render(request, 'shunchuang/index.html', {'active_index': 'active', 'form': loginform, 'user': name})

class Search():
    def search(self, request):
        login = Login()
        loginform = LoginForm()
        name = login.islogined(request)
        if request.method == 'POST':
            form = LoginForm(request.POST)
            result = login.loginfun(request, form)
            if result:
                return HttpResponseRedirect('/search/')
            return render(request, 'shunchuang/search.html', {'active_search': 'active', 'form': form, 'user': False})
        return render(request, 'shunchuang/search.html', {'active_search': 'active', 'form': loginform, 'user': name})

class ClassPage():
    def classpage(self, request):
        login = Login()
        loginform = LoginForm()
        name = login.islogined(request)
        if request.method == 'POST':
            form = LoginForm(request.POST)
            result = login.loginfun(request, form)
            if result:
                return HttpResponseRedirect('/class/')
            return render(request, 'shunchuang/class.html', {'active_class': 'active', 'form': form, 'user': False})
        return render(request, 'shunchuang/class.html', {'active_class': 'active', 'form': loginform, 'user': name})

class Auction():
    def auction(self, request):
        login = Login()
        loginform = LoginForm()
        name = login.islogined(request)
        if request.method == 'POST':
            form = LoginForm(request.POST)
            result = login.loginfun(request, form)
            if result:
                return HttpResponseRedirect('/auction/')
            return render(request, 'shunchuang/auction.html', {'active_auction': 'active', 'form': form, 'user': False})
        return render(request, 'shunchuang/auction.html', {'active_auction': 'active', 'form': loginform, 'user': name})

class Editinfo():
    def editinfo(self, request):
        login = Login()
        my    = My()
        name = login.islogined(request)
        if not name:
            return HttpResponseRedirect('/login/')

        userinfotab = my.getuserinfotab(request.user.username)
        editinfoform = EditinfoForm(initial=userinfotab)

        if request.method == 'POST':
            editinfoform = EditinfoForm(request.POST)
            if editinfoform.is_valid():
                username = editinfoform.cleaned_data['username']
                if username != request.user.username:
                    return HttpResponse('request not right')
                UserProfile.objects.filter(username__iexact=username).delete()
                editinfoform.save()
                userinfo = my.getuserinfo(request.user.username, True)
                return HttpResponseRedirect('/my/')
            else:
                return render(request, 'shunchuang/editinfo.html', {'active_my': 'active', 'user': name, 'userinfo': userinfo, 'editinfoform': editinfoform})

        return render(request, 'shunchuang/editinfo.html', {'active_my': 'active', 'user': name, 'editinfoform': editinfoform})

class Message():
    def message(self, request):
        login = Login()
        name = login.islogined(request)
        if request.method == 'POST':
            pass
        if not name:
            return HttpResponseRedirect('/login/')
        return render(request, 'shunchuang/message.html', {'active_class': 'active', 'user': name})

class My():
    def my(self, request):
        login = Login()
        loginform = LoginForm()
        name = login.islogined(request)
        if request.method == 'POST':
            form = LoginForm(request.POST)
            result = login.loginfun(request, form)
            if result:
                return HttpResponseRedirect('/my/')
            return render(request, 'shunchuang/my.html', {'active_my': 'active', 'form': form, 'user': False})
        if request.method == 'GET':
            try:    
                user = request.GET['user']
                userinfo = self.getuserinfo(user, False)
                if not userinfo:
                    return HttpResponse('用户不存在')
                return render(request, 'shunchuang/my.html', {'active_my': 'active', 'form': loginform, 'user': name, 'userinfo': userinfo})
            except KeyError:
                pass
        if not name:
            return HttpResponseRedirect('/login/')
        userinfo = self.getuserinfo(request.user.username, True)
        return render(request, 'shunchuang/my.html', {'active_my': 'active', 'form': loginform, 'user': name, 'userinfo': userinfo})

    def getuserinfotab(self, username):
        try:
            userinfo = UserProfile.objects.get(username = username)
        except ObjectDoesNotExist:
            return False
        username = userinfo.username
        name  = userinfo.name
        phone = userinfo.phone
        email = userinfo.email
        sex   = userinfo.sex
        age   = userinfo.age
        motto = userinfo.motto
        find  = userinfo.find
        hibby = userinfo.hibby
        city  = userinfo.city
        school       = userinfo.school
        school_class = userinfo.school_class
        which_class  = userinfo.which_class
        person_photo = userinfo.person_photo
        select = userinfo.select
        phone_show   = userinfo.phone_show
        email_show   = userinfo.email_show
        if not age:
            age = ''

        returnuserinfo = {'username':username, 'name':name, 'phone':phone, 'email':email, 'sex':sex, 'age':age, 'motto':motto, 'find':find, 'hibby':hibby, 'city':city, 'school':school, 'school_class':school_class, 'which_class':which_class, 'person_photo':person_photo, 'select':select, 'phone_show':phone_show, 'email_show':email_show}
        
        return returnuserinfo

    def getuserinfo(self, username, himself):
        try:
            userinfo = UserProfile.objects.get(username = username)
        except ObjectDoesNotExist:
            return False
        name  = userinfo.name
        phone = userinfo.phone
        email = userinfo.email
        sex   = userinfo.sex
        age   = userinfo.age
        motto = userinfo.motto
        find  = userinfo.find
        hibby = userinfo.hibby
        city  = userinfo.city
        school       = userinfo.school
        school_class = userinfo.school_class
        which_class  = userinfo.which_class
        person_photo = userinfo.person_photo
        select = userinfo.select
        phone_show   = userinfo.phone_show
        email_show   = userinfo.email_show
        
        if select == 1:
            select = '创业'
        else:
            select = '组队'
        if not age:
            age = ''
        if not himself:
            if not sex:
                sex = '保密'
            if not age:
                age = '保密'
            if not phone_show:
                phone = '保密'
            if not email_show:
                email = '保密'

        items =(('姓名',name), ('性别',sex), ('年龄',age), ('手机号',phone), ('邮箱',email), ('角色',select), ('寻找的队友',find), ('座右铭',motto), ('爱好/特长',hibby), ('城市',city), ('学校',school), ('专业',school_class), ('专业类别',which_class), ('个人相册',person_photo))
        returnuserinfo = OrderedDict(items) 
        return returnuserinfo

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
        name = self.islogined(request)
        if request.method == 'POST':
            form = LoginForm(request.POST)
            result = self.loginfun(request, form)
            if result:
                return HttpResponseRedirect('/my/')
            return render(request, 'shunchuang/login.html', {'user': False , 'form': form})

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
        login = Login()
        loginform = LoginForm()
        name = login.islogined(request)
        if request.method == 'GET':
            try:    
                verif = request.GET['verif']
                isexist = self.check_verif_get(request)
                return HttpResponse(isexist)
            except KeyError:
                return render(request, 'shunchuang/sign.html', {'signform': signform, 'form': loginform, 'user': name})

        if request.method == 'POST':
            formdo = request.POST['form']
            if formdo == 'login':
                loginform = LoginForm(request.POST)
                result = login.loginfun(request, loginform)
                if result:
                    return HttpResponseRedirect('/my/')
                return render(request, 'shunchuang/sign.html', {'signform': signform, 'form': loginform, 'user': name})
            if formdo == 'sign':
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
                return render(request, 'shunchuang/sign.html', {'signform': signform, 'form': loginform, 'user': name})

            return render(request, 'shunchuang/sign.html', {'signform': signform, 'form': loginform, 'user': name})

