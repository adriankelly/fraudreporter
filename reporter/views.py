from django.shortcuts import render
from .models import Case
from django.views import generic


# Create your views here.
class CaseDetailView(generic.DetailView):
    model = Case