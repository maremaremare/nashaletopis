# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView, View
from .models import *
import logging
logger = logging.getLogger('my')


class RadioView(View):

    def get_context_data(self, **kwargs):
        context = super(RadioView, self).get_context_data(**kwargs)
        context['categories'] = Radio_category.objects.all()
        context['categories_title'] = 'Категории радиопрограмм'
        context['announcements'] = Announcement_radio.objects.all()


        if self.kwargs.has_key('slug'):
            context['slug'] = self.kwargs['slug']
            context['category'] = get_object_or_404(
                Radio_category, slug=self.kwargs['slug']).title

        return context


class RadioListView(RadioView, ListView):
    template_name = 'radiolist.html'
    model = Radio


class RadioListByCategoryView(RadioListView):

    def get_queryset(self):
        self.category = get_object_or_404(
            Radio_category, slug=self.kwargs['slug'])
        return self.model.objects.filter(category=self.category)


class RadioDetailView(RadioView, DetailView):
    template_name = 'radiodetail.html'
    model = Radio
