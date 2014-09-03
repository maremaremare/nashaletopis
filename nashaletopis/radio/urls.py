# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import *
urlpatterns = patterns('radio.views',

                       url(
                           r'^$',
                           RadioListView.as_view(),
                           name='list'
                       ),

                       url(
                           r'(?P<slug>\S+)/(?P<pk>\d+)$',
                           RadioDetailView.as_view(),
                           name='detail'
                       ),

                       url(
                           r'(?P<slug>\S+)$',
                           RadioListByCategoryView.as_view(),
                           name='categorylist'
                       ),

                       

                       )
