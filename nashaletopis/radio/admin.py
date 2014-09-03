from django.contrib import admin
from .models import *



class RadioAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    list_display = ('__unicode__', 'date', 'category',)



admin.site.register(Radio, RadioAdmin)
admin.site.register(Radio_category)
admin.site.register(Announcement_radio)
