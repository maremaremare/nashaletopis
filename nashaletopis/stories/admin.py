# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

from autocomplete_light import modelform_factory
# class SomeAdmin(admin.ModelAdmin):
#    pass

from autocomplete_light.contrib.taggit_field import TaggitField, TaggitWidget



class PhotoInline(admin.StackedInline):
    model = Photo
    fields = ('photo', 'description')
    extra = 1
    ordering = ("photo",)


class VideoInline(admin.StackedInline):
    model = Video
    fields = ('title', 'video')
    extra = 1


class StoryAdmin(admin.ModelAdmin):
    list_filter = ('period', 'is_letter')
    list_display = ('name', 'get_periods', 'get_locations', 'is_letter',)

    form = modelform_factory(Story)
    form.tags = TaggitField(widget=TaggitWidget('TagAutocomplete'))
    inlines = [
        PhotoInline, VideoInline
    ]


class StoryActiveAdmin(StoryAdmin):
    list_filter = ('location', 'is_letter')
    list_display = ('name', 'location', 'is_letter',)
    form = modelform_factory(StoryActive)
    

#admin.site.register(SomeModel, SomeAdmin)
admin.site.register(History_period)
admin.site.register(Story, StoryAdmin)
admin.site.register(StoryActive, StoryActiveAdmin)

