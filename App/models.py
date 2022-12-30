from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Subject(models.Model):
    sid = models.AutoField(primary_key=True)
    sub_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.sub_name
    
class Personal(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    place  = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    def __str__(self):
        return self.name+" "+self.subject.sub_name
    
class ImageModel(models.Model):
    image = models.ImageField(upload_to = 'static/images/')