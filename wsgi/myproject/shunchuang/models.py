# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):

    WHICH_CLASS = (
        (u'管理类',u'管理类'),
        (u'计算机类',u'计算机类'),
        (u'机械类',u'机械类'),
        (u'外语类',u'外语类'),
        (u'中文类',u'中文类'),
        (u'建筑类',u'建筑类'),
        (u'艺术类',u'艺术类'),
        (u'物电类',u'物电类'),
        (u'数学类',u'数学类'),
        (u'材料类',u'材料类'),
        (u'文旅类',u'文旅类'),
        (u'生工类',u'生工类'),
    )

    username=models.CharField(max_length=20,blank=False) 
    name   = models.CharField(max_length=10,blank=True)
    sex  = models.CharField(max_length=4,blank=True)
    age    = models.IntegerField(null=True,blank=True)
    phone  = models.CharField(max_length=11,blank=False)
    phone_show = models.BooleanField(default=False,blank=False)
    email  = models.CharField(max_length=30,blank=False)
    email_show = models.BooleanField(default=True,blank=False)
    select = models.CharField(max_length=6,blank=False, choices=((u'创业', u'创业'),(u'组队', u'组队')))
    find   = models.CharField(max_length=200,blank=True)
    motto  = models.CharField(max_length=100,blank=True)
    hibby  = models.CharField(max_length=50,blank=True)
    city   = models.CharField(max_length=20,blank=True)
    school = models.CharField(max_length=20,blank=True)
    school_class = models.CharField(max_length=20,blank=True)
    which_class  = models.CharField(max_length=20,blank=True, choices=WHICH_CLASS)
    person_photo = models.IntegerField(default=0,blank=False)
    user_class   = models.IntegerField(default=1,blank=False)

    def __unicode__(self):
        return self.username

class Message(models.Model):
    id    = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30,blank=False)
    message   = models.TextField(blank=False)
    username  = models.CharField(max_length=20,blank=False)
    name      = models.CharField(max_length=10,blank=False)
    reply     = models.TextField(blank=True)
    replyname = models.CharField(max_length=20,blank=True)

    def __unicode__(self):
        return self.title
    
class News(models.Model):
    id    = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,blank=False)
    url = models.CharField(max_length=60,blank=True)

    def __unicode__(self):
        return self.title
    
class Crowdfund(models.Model):
    id    = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,blank=False)
    url = models.CharField(max_length=60,blank=True)

    def __unicode__(self):
        return self.title
    
