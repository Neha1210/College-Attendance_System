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

class HODForm(ModelForm):
    class Meta:
        model=HOD
        fields='__all__'

class DefaulterForm(ModelForm):
    defaulter_list=models.CharField(max_length=200,null=True)
    extra_field_count=forms.CharField(widget=forms.HiddenInput())

    def __init__(self,*args,**kwargs):
        extra_fields=kwargs.pop('extra',0)

        super(DefaulterForm,self).__init__(*args,**kwargs)
        self.fields['extra_field_count'].initial=extra_fields

        for index in range(int(extra_fields)):
            self.fields['extra_field_{index}'.format(index=index)]=forms.CharField()

    class Meta:
        model=defaulter
        fields='__all__'