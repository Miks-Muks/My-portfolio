from django.shortcuts import render
from .models import Project


# Create your views here.

def home(request):
    projects = Project.objects.all()
    # project = Project.objects.get(id=4)
    return render(request, 'portfolio/home.html', {'projects': projects})


