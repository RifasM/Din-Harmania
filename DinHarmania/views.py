from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


class Homepage(TemplateView):
    template_name = 'index.html'
# Create your views here.
