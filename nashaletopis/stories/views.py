# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView, View
from .models import *
from locations.models import Location
from locations.views import relatedCount
import logging
from taggit.models import Tag

# Get an instance of a logger
logger = logging.getLogger('my')


class StoriesView(View):

    def get_context_data(self, **kwargs):
        context = super(StoriesView, self).get_context_data(**kwargs)
        if self.model != StoryActive:
            context['periods'] = relatedCount(
                History_period, self.model, 'period', 'o_count')
        context['locations'] = relatedCount(
            Location, self.model, 'location', 'l_count')
        if self.kwargs.has_key('slug'):
            context['slug'] = self.kwargs['slug']
            context['periodname'] = get_object_or_404(
                History_period, slug=self.kwargs['slug']).name
        if self.kwargs.has_key('locationpk'):
            context['locationpk'] = self.kwargs['locationpk']
            context['location'] = get_object_or_404(
                Location, id=self.kwargs['locationpk']).title
            logger.info(context['location'])
        if self.kwargs.has_key('tag'):
            context['tagslug'] = self.kwargs['tag']
            context['tagitem'] = Tag.objects.get(slug=self.kwargs['tag']).name
        return context


class StoriesListView(StoriesView, ListView):
    model = Story
    template_name = "storieslist.html"


class TagView(object):

    def get_queryset(self):
        return self.model.objects.filter(tags__slug__in=[self.kwargs['tag']])


class StoriesTagListView(TagView, StoriesListView):
    pass


class StoryDetailView(StoriesView, DetailView):
    model = Story
    template_name = "story.html"


class StoriesLettersView(StoriesView, ListView):
    template_name = "storieslist.html"

    def get_queryset(self):
        return self.model.objects.filter(is_letter=True)


class StoriesByPeriodView(StoriesView, ListView):
    template_name = "storieslist.html"

    def get_queryset(self):
        self.period = get_object_or_404(
            History_period, slug=self.kwargs['slug'])
        return Story.objects.filter(period__id__exact=self.period.id)

    def get_context_data(self, **kwargs):
        context = super(StoriesByPeriodView, self).get_context_data(**kwargs)

        context['urlconstruct'] = 'period'

        return context


class StoriesByLocationView(StoriesView, ListView):
    template_name = "storieslist.html"

    def get_queryset(self):
        self.location = get_object_or_404(
            Location, id=self.kwargs['locationpk']).get_descendants(include_self=True)
        # чтобы children
        return self.model.objects.filter(location=self.location).distinct()

    def get_context_data(self, **kwargs):
        context = super(StoriesByLocationView, self).get_context_data(**kwargs)

        context['urlconstruct'] = 'location'

        return context


from django import forms
from captcha.fields import CaptchaField


class SendStoryForm(forms.Form):
    sent_by = forms.CharField(max_length=100, label=u'Ваше имя')
    name = forms.CharField(max_length=100, label=u'Имя человека')
    sender = forms.EmailField(label=u'Ваш емэйл')
    text = forms.CharField(label=u'Текст истории', widget=forms.Textarea)
    url = forms.URLField(
        label=u'Ссылка на архив с фотографиями', required=False)
    captcha = CaptchaField(label=u'Вы случайно не робот? Решите, пожалуйста, пример')


    def send_email(self):
            sent_by = self.cleaned_data['sent_by']
            sender = self.cleaned_data['sender']
            name = self.cleaned_data['name']
            text = self.cleaned_data['text']
            url = self.cleaned_data['url']

            from django.core.mail import send_mail
            send_mail(u'Посетитель сайта nashaletopis.ru прислал новую историю', u'Кто прислал: ' + sent_by + u' (' + sender +
                      u')\n\nИмя человека: ' + name + u'\n\nCcылка на фотографии: '+url+u'\n\n\n\n\n' + text, 'НашаЛетопись.ru', ('ksawie@gmail.com',))
        # send email using the self.cleaned_data dictionary
     

    

from django.views.generic.edit import FormView

class ThanksView(StoriesView, TemplateView):
    template_name='thanks.html'
    model = Story

class SendStoryView(StoriesView, FormView):
    template_name = 'sendstory.html'
    form_class = SendStoryForm
    success_url = '/stories/thanks'
    model = Story

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(SendStoryView, self).form_valid(form)
