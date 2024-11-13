from django.db import models

class MyDetails(models.Model):
    paragraph = models.CharField(max_length=250)
    experience = models.FloatField(default=0)
    completedprojects = models.IntegerField(default=0)
    awards = models.IntegerField(default=0)
    clients = models.IntegerField(default=0)
    logo = models.ImageField(null=True)
    myimage = models.ImageField(null=True, blank=True)
    
class About(models.Model):
    stackimage = models.ImageField(null=True, blank=False) 
    stackname = models.CharField(max_length=100, default='')
      
    def __str__(self):
        return f"{self.stackname}"
    