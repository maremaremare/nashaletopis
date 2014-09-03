from django.shortcuts import render

from django.views.generic import ListView, TemplateView, DetailView
from .models import *

class HelpListView(ListView):
    template_name = "helpuslist.html"
    model = HelpItem

class HelpDetailView(DetailView):
    model = HelpItem
    template_name = "helpusdetail.html" 