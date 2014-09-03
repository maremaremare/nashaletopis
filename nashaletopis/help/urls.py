# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import *
urlpatterns = patterns('help.views',

                       url(
                           r'^$',
                           HelpListView.as_view(),
                           name='list'
                       ),

                       url(
                           r'(?P<slug>\S+)$',
                           HelpDetailView.as_view(),
                           name='detail'
                       ),
                       

                       )
