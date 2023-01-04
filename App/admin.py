from django.contrib import admin
from App.models import Subject,Personal,ImageModel
# Register your models here.



admin.site.register(Subject)
admin.site.register(Personal)
# admin.site.register(ImageModel)

@admin.register(ImageModel)
class imagemodel(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display=('image',)  
     
    
