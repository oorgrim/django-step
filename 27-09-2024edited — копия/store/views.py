from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

class MainPageView(TemplateView):
    template_name = "mainpage/index.html"
