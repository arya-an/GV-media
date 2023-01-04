# from django import forms
# from App.models import ImageModel
# from django.conf import settings
# # from django.utils.image import Image
# import Image



# class UploadImageForm(forms.ModelForm):
#     class Meta:
#         model = ImageModel
#         fields = ['image']
        
#     def clean_photo(self):
#         image = self.cleaned_data.get(['image'])
#         if image:
#             format = Image.open(image.file).format
#             image.file.seek(0)
#             if format in settings.VALID_IMAGE_FILETYPES:
#                 return image
#         raise forms.ValidationError('FileType not supported: only upload jpegs and pngs.')