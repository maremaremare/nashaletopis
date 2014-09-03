# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView, View
from .models import *
from locations.models import Location
from locations.views import relatedCount
# Create your views here.


class MapGeneralView(TemplateView):
    template_name = "generalhelpmap.html"

    def render_to_response(self, context, **response_kwargs):
        response = super(MapGeneralView, self).render_to_response(
            context, **response_kwargs)
        if self.kwargs.has_key('xml'):
            response['Content-Type'] = 'text/xml; charset=utf-8'
        return response

    def get_context_data(self, **kwargs):
        context = super(MapGeneralView, self).get_context_data(**kwargs)
        context['helpneeded'] = HelpNeeded.objects.all()
        context['helpgiven'] = HelpingOrganisation.objects.all()
        return context


class HelpGivenView(View):

    def get_context_data(self, **kwargs):

        context = super(HelpGivenView, self).get_context_data(**kwargs)
        context['color'] = '#0095b6'
        context['locations'] = relatedCount(
            Location, self.model, 'location', 'l_count')
        context['categories'] = HelpingCategory.objects.all()
        context['categories_title'] = 'Категории помогающих организаций'
        if self.kwargs.has_key('locationpk'):
            context['locationpk'] = self.kwargs['locationpk']
            context['location'] = get_object_or_404(
                Location, id=self.kwargs['locationpk']).title
            context['l'] = get_object_or_404(
                Location, id=self.kwargs['locationpk'])
        if self.kwargs.has_key('slug'):
            context['slug'] = self.kwargs['slug']
            context['category'] = get_object_or_404(
                HelpingCategory, slug=self.kwargs['slug']).title
        # if self.kwargs.has_key('tag'):
        #     context['tagslug'] = self.kwargs['tag']
        #     context['tagitem'] = Tag.objects.get(slug=self.kwargs['tag']).title
        return context


class HelpGivenListView(HelpGivenView, ListView):
    template_name = 'givenhelpmap.html'
    model = HelpingOrganisation


class HelpGivenByLocationListView(HelpGivenListView):

    def get_queryset(self):
        self.location = get_object_or_404(
            Location, id=self.kwargs['locationpk']).get_descendants(include_self=True)
        # чтобы children
        return self.model.objects.filter(location=self.location).distinct()


class HelpGivenByCategoryListView(HelpGivenListView):

    def get_queryset(self):
        self.category = get_object_or_404(
            HelpingCategory, slug=self.kwargs['slug'])
        # чтобы children
        return self.model.objects.filter(category=self.category)


class HelpGivenDetailView(HelpGivenView, DetailView):
    template_name = 'givenhelpmapdetail.html'
    model = HelpingOrganisation


class HelpNeededView(View):

    def get_context_data(self, **kwargs):

        context = super(HelpNeededView, self).get_context_data(**kwargs)
        context['color'] = 'red'
        context['locations'] = relatedCount(
            Location, self.model, 'location', 'l_count')

        if self.kwargs.has_key('locationpk'):
            context['locationpk'] = self.kwargs['locationpk']
            context['location'] = get_object_or_404(
                Location, id=self.kwargs['locationpk']).title
            context['l'] = get_object_or_404(
                Location, id=self.kwargs['locationpk'])
        return context


class HelpNeededListView(HelpNeededView, ListView):
    template_name = 'neededhelpmap.html'
    model = HelpNeeded


class HelpNeededByLocationListView(HelpNeededListView):

    def get_queryset(self):
        self.location = get_object_or_404(
            Location, id=self.kwargs['locationpk']).get_descendants(include_self=True)
        # чтобы children
        return self.model.objects.filter(location=self.location).distinct()

class HelpNeededClosedListView(HelpNeededListView):

    def get_queryset(self):
        return self.model.objects.filter(opened=False)


class HelpNeededDetailView(HelpNeededView, DetailView):
    template_name = 'neededhelpmapdetail.html'
    model = HelpNeeded