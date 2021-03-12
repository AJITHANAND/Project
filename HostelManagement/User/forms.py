from .models import *
from django import forms


class Register(forms.ModelForm):
    class Meta:
        model = register_new_user
        fields = ['email', 'password', 'fname', 'lname', 'phone', 'address', 'course', 'year', 'admno']


class contact_us(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = ['uname', 'uemail', 'uphone', 'umsg']
