from django.urls import path
from rest_framework.authtoken import views

from App.views import *



urlpatterns = [
    
    path('',SubjectCreate.as_view(),name='subjectcreate'),
    path('<int:pk>',SubjectDetails.as_view(),name='subjectdetail'),
    path('all/',AllSubject.as_view(),name='allsubject'),
    path('personal',PersonalCreate.as_view(),name='personalcreate'),
    path('personal/<int:pk>',PersonalDetails.as_view(),name='personaldetail'),
    path('personal/all/',AllPersonal.as_view(),name='allpersonal'),
    path('auth/',views.obtain_auth_token),
    path('reg/',registerUser.as_view(),name='registeruser'),
    
    
]