from django.shortcuts import render
from .models import Point, History
from django.views import generic


def index(request):
    return render(request, 'points/index.html')

def new_form(request):
    return render(request, 'points/new.html')

def submit_form(request):    
    return render(request, 'points/history.html')

class NewView(generic.DetailView):
    model = Point
    template_name = 'points/new.html'

class HistoryView(generic.ListView):
    model = Point
    template_name = 'points/history.html'
    # return render(request, 'points/history.html')

