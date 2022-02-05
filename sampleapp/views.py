from django.shortcuts import render
from django.views.generic.list import ListView
from .models import SampleAppModel

# Create your views here.

class SampleAppList(ListView):
    template_name = 'list.html'
    model = SampleAppModel