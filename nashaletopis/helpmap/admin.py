from django.contrib import admin
from .models import *

class OrgAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    list_display = ('__unicode__', 'location', 'category','phone','address')

class HelpAdmin(admin.ModelAdmin):
    list_filter = ('opened',)
    list_display = ('title', 'location', 'opened')


# Register your models here.
admin.site.register(HelpingCategory)
admin.site.register(HelpingOrganisation, OrgAdmin) 
admin.site.register(HelpNeeded, HelpAdmin)
