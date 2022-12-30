from rest_framework import serializers
from App.models import Personal,Subject
from django.contrib.auth.models import User




class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subject
        fields = ('sid','sub_name','description')
        



class PersonalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Personal
        fields = ('pid','name','place','subject')
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']
        
