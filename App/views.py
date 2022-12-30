from django.shortcuts import render
from App.serializers import SubjectSerializer,PersonalSerializer,UserSerializer
from App.models import Subject,Personal,User
from rest_framework import generics
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

### ALL crud poerations for both models

class SubjectCreate(generics.CreateAPIView):
    queryset2 = Subject.objects.all()
    serializer_class = SubjectSerializer
    
class SubjectDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class AllSubject(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
    
class PersonalCreate(generics.CreateAPIView):
    queryset2 = Personal.objects.all()
    serializer_class = PersonalSerializer
    
class PersonalDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
 
#to get the related fields
    
class AllPersonal(generics.ListAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['subject__sid']
  
  
#token generation
  
class registerUser(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':'Some thing went wrong'})
        serializer.save()
        
        user = User.objects.get(username = serializer.data['username'])
        token_obj , _ = Token.objects.get_or_create(user=user)
        return Response({'details':serializer.data,'token' : str(token_obj)})
    
    
  
# def clean_photo(self):
#         photo = self.cleaned_data.get(['photo'])
#         if photo:
#             format = Image.open(photo.file).format
#             photo.file.seek(0)
#             if format in settings.VALID_IMAGE_FILETYPES:
#                 return photo
#         raise forms.ValidationError(...)