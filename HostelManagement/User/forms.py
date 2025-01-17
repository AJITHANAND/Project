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
class Student_add(forms.ModelForm):
    class Meta:
        model = student
        fields =['sd_name','sd_admno','sd_course','sd_year','sd_dob','sd_email','sd_guardian','sd_address','sd_room_no','sd_phone','sd_guardian_phone','sd_parent','sd_parent_phone','sd_password']
class Student_edit(forms.ModelForm):
    class Meta:
        model =student
        fields =['sd_name','sd_admno','sd_course','sd_year','sd_email','sd_guardian','sd_address','sd_room_no','sd_phone','sd_guardian_phone','sd_parent','sd_parent_phone','sd_password']

class complaints(forms.ModelForm):
    class Meta:
        model=complaint
        fields=['auther','auther_phone','auther_ID','subject','status','date','body']

class add_fee_ind(forms.ModelForm):
    class Meta:
        model = fees
        fields=['sd_id','mess_fee','fine','accommodation','common','total']