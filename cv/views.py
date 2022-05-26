from django.shortcuts import render

from django.views.generic import ListView
from .models import Cv

# Create your views here.

class CvView(ListView):
    model = Cv
    template_name = 'CV.html'
