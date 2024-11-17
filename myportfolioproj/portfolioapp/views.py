from django.shortcuts import render
from django.http import request,HttpResponse
from .models import MyDetails, About, Services, Projects, Testimonials

from django.core.mail import send_mail
from django.conf import settings

import threading

class EmailThread(threading.Thread):
    def __init__(self, send_mail):
        self.send_mail = send_mail
        threading.Thread.__init__(self)
    
    def run(self):
        email_message.send()

def index(request):
    details = MyDetails.objects.all()
    return render(request, 'index.html', {'details':details})

def aboutprofile(request):
    myprofile = AboutProfile.objects.all()
    return render(request, 'about.html', {'myprofile':myprofile})

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
    return render(request, 'testimonials.html',{'myclients':myclients})

def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        phone = request.POST['phone']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        send_mail = EmailMessage(
            lname,
            phone,
            message,
            'settings.EMAIL_HOST_USER',
            [email]
        )
        
        EmailThread(send_mail).start()
    return render(request, 'contact.html')
