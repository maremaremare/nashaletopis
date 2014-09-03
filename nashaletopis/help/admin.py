from django.contrib import admin

# Register your models here.
from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from .models import HelpItem

class ItemAdmin(OrderedModelAdmin):
    list_display = ('title', 'move_up_down_links')

admin.site.register(HelpItem, ItemAdmin)