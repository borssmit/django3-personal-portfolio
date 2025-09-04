from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, '/home/bors/django_projects/personal_portfolio_project/portfolio/templates/portfolio/home.html', {'projects':projects}) 