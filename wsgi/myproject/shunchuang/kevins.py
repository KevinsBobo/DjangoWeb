# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from shunchuang.models import UserProfile


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

