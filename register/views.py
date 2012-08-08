# Create your views here.
from django.shortcuts import render
from register import models

def index(request):
    return render(request, 'index.html', {})

def attendants(request):
    return render(request, 'attendants.html', {})

def organizers(request):
    return render(request, 'organizers.html', {})

def program(request):
    return render(request, 'program.html', {})

def report(request):
    return render(request, 'report.html', {})

def venue(request):
    return render(request, 'venue.html', {})

def register(request):
    if request.method == 'POST':
        form = models.RegistrantForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = models.RegistrantForm()
        
    return render(request, 'register.html', {'form': form})