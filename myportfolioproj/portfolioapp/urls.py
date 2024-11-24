
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('projects', views.projects, name="projects"),
    path('testimonials', views.testimonials, name="testimonials"),
    path('contact', views.contact, name="contact"),
    path('admin-dashboard', views.admin_dashboard, name="admin-dashboard"),
]
   
