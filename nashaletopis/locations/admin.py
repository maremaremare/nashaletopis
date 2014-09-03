# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

from django_ymap.admin import YmapAdmin


from django_mptt_admin.admin import DjangoMpttAdmin


class LocationAdmin(YmapAdmin, DjangoMpttAdmin):
    list_display = ['title', 'address']
    


admin.site.register(Location, LocationAdmin)
