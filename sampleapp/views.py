from django.shortcuts import render
from django.views.generic.list import ListView
from .models import SampleAppModel

# Create your views here.

class SampleAppTest(ListView):
    template_name = 'test.html'
    model = SampleAppModel