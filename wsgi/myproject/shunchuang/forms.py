# -*- coding:utf-8 -*-
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from shunchuang.models import UserProfile

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

