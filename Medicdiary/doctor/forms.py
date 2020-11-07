from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import DoctorProfile

class DoctorRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(help_text='Your password can’t be too similar to your other personal information. <br>Your password must contain at least 8 characters.<br>Your password can’t be a commonly used password.<br>Your password can’t be entirely numeric.')

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ('name','phone','Specialisation','City','Registration_Number','Registration_Council','Registration_year','Degree','College','Year_of_completion','Medical_registration_proof','Current_place_of_work','Gender','Profile_pic','Aadhar_Number')
