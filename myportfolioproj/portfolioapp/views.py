from django.shortcuts import render
from django.http import request,HttpResponse
from .models import MyDetails, About, Services, Projects, Testimonials


def index(request):
    details = MyDetails.objects.all()
    return render(request, 'index.html', {'details':details})

def about(request):
    myabout = About.objects.all()
    return render(request, 'about.html', {'myabout':myabout})

def services(request):
    myservices = Services.objects.all()
    return render(request, 'services.html', {'myservices':myservices})

def projects(request):
    myprojects = Projects.objects.all()
    return render(request, 'projects.html',{'myprojects':myprojects})

def testimonials(request):
    myclients = Testimonials.objects.all()
    return render(request, 'testimonials.html')

def contact(request):
    return render(request, 'contact.html')
