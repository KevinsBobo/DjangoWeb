from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    username=models.CharField(max_length=20,blank=False) 
    name   = models.CharField(max_length=10,blank=True)
    phone  = models.CharField(max_length=11,blank=False)
    email  = models.CharField(max_length=30,blank=False)
    select = models.BooleanField(blank=False)
    age    = models.IntegerField(null=True,blank=True)
    motto  = models.CharField(max_length=100,blank=True)
    find   = models.CharField(max_length=200,blank=True)
    hibby  = models.CharField(max_length=50,blank=True)
    city   = models.CharField(max_length=20,blank=True)
    school = models.CharField(max_length=20,blank=True)
    school_class = models.CharField(max_length=20,blank=True)
    which_class  = models.CharField(max_length=20,blank=True)
    person_photo = models.CharField(max_length=30,blank=True)
    user_class   = models.IntegerField(default=1,blank=False)

    def __unicode__(self):
        return self.username

