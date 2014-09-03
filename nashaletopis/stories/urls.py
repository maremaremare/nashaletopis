# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import *
urlpatterns = patterns('stories.views',
                       url(
                           r'send$',
                           SendStoryView.as_view(),
                           name='send'
                       ),

                       url(
                           r'thanks$',
                           ThanksView.as_view(),
                           name='thanks'
                       ),
                       url(
                           r'active/location/(?P<locationpk>\d+)$',
                           StoriesByLocationView.as_view(model=StoryActive),
                           name='actplace'
                       ),
                       url(
                           r'location/(?P<locationpk>\d+)$',
                           StoriesByLocationView.as_view(model=Story),
                           name='place'
                       ),
                       url(
                           r'period/(?P<slug>\S+)/read/(?P<pk>\d+)$',
                           StoryDetailView.as_view(model=Story),
                           name='storybyperiod'
                       ),
                       url(
                           r'active/location/(?P<locationpk>\d+)/read/(?P<pk>\d+)$',
                           StoryDetailView.as_view(model=StoryActive),
                           name='activestorybylocation'
                       ),
                       url(
                           r'location/(?P<locationpk>\d+)/read/(?P<pk>\d+)$',
                           StoryDetailView.as_view(model=Story),
                           name='storybylocation'
                       ),

                       url(
                           r'^$',
                           StoriesListView.as_view(model=Story),
                           name='stories'
                       ),

                       url(
                           r'tags/(?P<tag>\S+)$',
                           StoriesTagListView.as_view(model=Story),
                           name='storiestag'
                       ),

                       url(
                           r'tags/(?P<tag>\S+)$',
                           StoriesTagListView.as_view(model=StoryActive),
                           name='activestoriestag'
                       ),

                       url(
                           r'period/(?P<slug>\S+)$',
                           StoriesByPeriodView.as_view(model=Story),
                           name='period'
                       ),


                       url(
                           r'active/read/(?P<pk>\d+)$',
                           StoryDetailView.as_view(model=StoryActive),
                           name='activestory'
                       ),

                       url(
                           r'read/(?P<pk>\d+)$',
                           StoryDetailView.as_view(model=Story),
                           name='story'
                       ),

                       url(
                           r'active/letters/$',
                           StoriesLettersView.as_view(model=StoryActive),
                           name='activeletters'
                       ),

                       url(
                           r'letters/$',
                           StoriesLettersView.as_view(model=Story),
                           name='letters'
                       ),





                       url(
                           r'active/$',
                           StoriesListView.as_view(model=StoryActive),
                           name='active stories'
                       ),

                       )
