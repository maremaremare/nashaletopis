# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import *
urlpatterns = patterns('helpmap.views',
                       url(
                           r'^$',
                           MapGeneralView.as_view(),
                           name='general'
                       ),

                       url(
                           r'helpgiven/$',
                           HelpGivenListView.as_view(),
                           name='givenlist'
                       ),



                       url(
                           r'helpgiven/(?P<locationpk>\d+)/(?P<pk>\d+)$',
                           HelpGivenDetailView.as_view(),
                           name='givendetail'
                       ),

                       url(
                           r'helpgiven/location/(?P<locationpk>\d+)$',
                           HelpGivenByLocationListView.as_view(),
                           name='givenlocationlist'
                       ),



                       url(
                           r'helpgiven/(?P<slug>\w+)$',
                           HelpGivenByCategoryListView.as_view(),
                           name='givencategorylist'
                       ),

                       url(
                           r'helpneeded/$',
                           HelpNeededListView.as_view(),
                           name='neededlist'
                       ),

                       url(
                           r'helpneeded/closed$',
                           HelpNeededClosedListView.as_view(template_name="closedmap.html"),
                           name='neededclosedlist'
                       ),


                      url(
                           r'helpneeded/(?P<locationpk>\d+)/(?P<pk>\d+)$',
                           HelpNeededDetailView.as_view(),
                           name='neededdetail'
                       ),

                       url(
                           r'helpneeded/location/(?P<locationpk>\d+)$',
                           HelpNeededByLocationListView.as_view(),
                           name='neededlocationlist'
                       ),



                       )
