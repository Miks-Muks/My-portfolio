from django.shortcuts import render
from .models import Project


# Create your views here.

def home(request):
    projects = Project.objects.filter(framework=1).select_related('framework')
    project = Project.objects.get(id=4)
    return render(request, 'portfolio/home.html', {'projects': projects, 'p': project, 'tests': p})
