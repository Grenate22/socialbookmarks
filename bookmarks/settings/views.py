from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class SettingHomeView(TemplateView):
    template_name='settings.html'