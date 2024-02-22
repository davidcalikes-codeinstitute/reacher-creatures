from django.shortcuts import render
from django.views import generic

class HomePage(generic.TemplateView):
    """
    Displays hero carousel and CTA to about page"
    """
    template_name = 'index.html'
    