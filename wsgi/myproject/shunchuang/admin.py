from django.contrib import admin
from .models import Person
from .models import UserProfile
from shunchuang.models import Message
from shunchuang.models import News
from shunchuang.models import Crowdfund

# Register your models here.

admin.site.register(Person)

admin.site.register(UserProfile)

admin.site.register(Message)
                    
admin.site.register(Crowdfund)

admin.site.register(News)
