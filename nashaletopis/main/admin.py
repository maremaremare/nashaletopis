from django.contrib import admin
from solo.admin import SingletonModelAdmin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import *

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Mainpage, SingletonModelAdmin)
admin.site.register(TeamMember)
# Register your models here.
