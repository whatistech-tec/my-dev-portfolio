from django.shortcuts import render
from django.http import request,HttpResponse
from .models import MyDetails, About


def index(request):
    details = MyDetails.objects.all()
    return render(request, 'index.html', {'details':details})

def about(request):
    stack = About.objects.all()
    return render(request, 'about.html', {'stack':stack})

def services(request):
    return render(request, 'services.html')

def projects(request):
    return render(request, 'projects.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def contact(request):
    return render(request, 'contact.html')
