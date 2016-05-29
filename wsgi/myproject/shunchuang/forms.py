# -*- coding:utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from shunchuang.models import UserProfile
from shunchuang.models import Message
from shunchuang.models import News
from shunchuang.models import Crowdfund
import re

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'message', 'username', 'name']
        labels = {
            'title'  : _(u'标题'),        
            'message': _(u'内容'),        
        }

class ReplyForm(forms.Form):
    id = forms.IntegerField(label='留言编号')
    reply = forms.CharField(label='回复')
    replyname = forms.CharField(label='回复者', max_length=20)
    
    def clean_id(self):
        id = self.cleaned_data['id']
        try:
            Message.objects.get(id = id)
        except ObjectDoesNotExist:
            raise forms.ValidationError('该编号留言不存在')
        return id

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'url']
        labels = {
            'title'  : _(u'标题(必填)'),        
            'message': _(u'内容(选填)'),        
        }

class CrowdForm(ModelForm):
    class Meta:
        model = Crowdfund
        fields = ['title', 'url']
        labels = {
            'title'  : _(u'标题(必填)'),        
            'message': _(u'内容(选填)'),        
        }

class EditinfoForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user_class']
        labels = {
            'name'   : _(u'姓名'),
            'sex'    : _(u'性别'),
            'age'    : _(u'年龄'),
            'phone'  : _(u'手机'),
            'email'  : _(u'邮箱'),
            'select' : _(u'角色'),
            'find'   : _(u'寻找的队友'),
            'motto'  : _(u'座右铭'),
            'hibby'  : _(u'爱好/特长'),
            'city'   : _(u'城市'),
            'school' : _(u'学校'),
            'school_class' : _(u'专业'),
            'which_class'  : _(u'专业类别'),
            'person_photo' : _(u'个人相册'),
            'phone_show'   : _(u'手机号对其他用户可见'),
            'email_show'   : _(u'邮箱对其他用户可见'),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        return name

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('用户名中只能包含字母、数字和下划线')
        return username

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        username = self.cleaned_data['username']
        vephone = UserProfile.objects.filter(phone=phone).exclude(username__iexact = username)
        isexist = vephone.exists() 

        if isexist:
            raise forms.ValidationError('手机号已注册')
        return phone

    def clean_email(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        veemail = UserProfile.objects.filter(email__iexact=email).exclude(username__iexact = username)
        isexist = veemail.exists() 

        if isexist:
            raise forms.ValidationError('邮箱已注册')
        return email
    

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
    select    = forms.ChoiceField(label='选择角色', choices=(('创业', '创业'),('组队', '组队')), widget=forms.RadioSelect())
    
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
