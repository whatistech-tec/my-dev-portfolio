from django.db import models

class MyDetails(models.Model):
    paragraph = models.CharField(max_length=250)
    experience = models.FloatField(default=0)
    completedprojects = models.IntegerField(default=0)
    awards = models.IntegerField(default=0)
    clients = models.IntegerField(default=0)
    logo = models.ImageField(null=True)
    myimage = models.ImageField(null=True, blank=True)
    
# class AboutProfile(models.Model):
#     profileimage = models.ImageField(null=True, upload_to='stack/')
#     span = models.CharField(max_length=80)
#     subtitle = models.CharField(max_length=80)
#     profilebio = models.CharField(max_length=250)
    
class About(models.Model):
    stackimage = models.ImageField(null=True, upload_to='stack/') 
    stackname = models.CharField(max_length=50)
      
    def __str__(self):
        return f"{self.stackname}"
    
class Services(models.Model):
    icon = models.CharField(max_length=80)
    service = models.CharField(max_length=50)
    servicedesc = models.CharField(max_length=250)
    
    def __str__(self):
        return f"{self.service}"
    
class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    projectname = models.CharField(max_length=80)
    projectfilter = models.CharField(max_length=50)
    projectdesc = models.CharField(max_length=250)
    projectimg = models.ImageField(null=False, upload_to='projects/')
    
    def __str__(self):
        return f"{self.projectname}"
    
class Testimonials(models.Model):
    clientname = models.CharField(max_length=80)
    clientposition = models.CharField(max_length=80)
    clientcompany = models.CharField(max_length=80)
    clientview = models.CharField(max_length=250)
    clientimg = models.ImageField(null=False, upload_to='projects/')
    
    def __str__(self):
        return f"{self.clientname}"
    
