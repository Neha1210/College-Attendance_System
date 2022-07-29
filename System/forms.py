from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms

class UploadForm(ModelForm):
    class Meta:
        model=Upload
        fields='__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class FacultyForm(ModelForm):
    class Meta:
        model=faculty
        fields='__all__'

class AttendanceForm(ModelForm):
    class Meta:
        model=attendance
        fields=['stud','asub','Remark']