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

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

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

def admin_dashboard(request):
    # myadmin = Testimonials.objects.all()
    return render(request, 'admin-dashboard.html')

def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        phone = request.POST['phone']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        context = {
            'firstname':firstname,
            'lastname':lastname,
            'email':email,
            'phone':phone,
            'message':message
        }
        
        message = """
        
        New Message: {}
        
        From {}:
        """.format(context['message'], context['email'] )
        send_mail(
            lastname,
            phone,
            message, '', ['nyandaruahesborn5@gmail.com']
        #     'settings.EMAIL_HOST_USER',
        #     [email],
        #     fail_silently=False,
        #     html_message=message
        )
        
    return render(request, 'contact.html', {})
