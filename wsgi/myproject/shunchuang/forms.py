# -*- coding:utf-8 -*-
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from shunchuang.models import UserProfile
import re

class LoginForm(forms.Form):
    phone = forms.CharField(label='手机', max_length=11)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        try:
            UserProfile.objects.get(phone = phone)
        except ObjectDoesNotExist:
            raise forms.ValidationError('该手机号未注册')
        return phone

class SignForm(forms.Form):
    username  = forms.CharField(label='用户名', max_length=20)
    passwordo = forms.CharField(label='密码', widget=forms.PasswordInput())
    passwordt = forms.CharField(label='确认密码', widget=forms.PasswordInput())
    phone     = forms.CharField(label='手机', max_length=11)
    email     = forms.EmailField(label='电子邮件')
    select    = forms.ChoiceField(label='选择角色', choices=((1, '创业'),(2, '组队')), widget=forms.RadioSelect())
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('用户名中只能包含字母、数字和下划线')

        veusername = UserProfile.objects.filter(username__iexact=username)
        isexist = veusername.exists() 

        if isexist:
            raise forms.ValidationError('用户名已存在')
        return username

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        vephone = UserProfile.objects.filter(phone=phone)
        isexist = vephone.exists() 

        if isexist:
            raise forms.ValidationError('手机号已注册')
        return phone

    def clean_email(self):
        email = self.cleaned_data['email']
        veemail = UserProfile.objects.filter(email__iexact=email)
        isexist = veemail.exists() 

        if isexist:
            raise forms.ValidationError('邮箱已注册')
        return email

    def clean_passwordt(self):
        passwordo = self.cleaned_data['passwordo']
        passwordt = self.cleaned_data['passwordt']
        if passwordo == passwordt:
            return passwordt
        raise forms.ValidationError('密码不匹配')
