from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.utils.html import mark_safe
from django.utils.functional import cached_property
from django.utils.html import format_html


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
    image = models.ImageField(upload_to = 'static/images/', validators=[FileExtensionValidator(['jpg','png'])])
    def img_preview(self): 
        return mark_safe(f'<img src = "{self.image.url}"/>')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # @cached_property
    # def display_image(self):
    #     html = '<img src="{img}">'
    #     if self.image:
    #         return format_html(html, img=self.image.url)
    #     return format_html('<strong>There is no image for this entry.<strong>')
    # display_image.short_description = 'Display image'
    # def img_preview(self): #new
    #     return mark_safe('<img src = "{url}" width = "300"/>'.format(
    #          url = self.image.url
    #      ))
    
    