from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PatientProfile, PatientVitals



class PatientRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=64)
    password1 = forms.CharField(help_text='Your password can’t be too similar to your other personal information. <br>Your password must contain at least 8 characters.<br>Your password can’t be a commonly used password.<br>Your password can’t be entirely numeric.')

    class Meta:             
        model = User
        # widgets = {'usertype': forms.HiddenInput()}
        fields = ['username','email','password1','password2']
        # exclude = ['usertype']

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ('name','age','gender','address','phone','emergency_contact','profession','profile_pic','Aadhar_Number')


class PatientVitalsForm(forms.ModelForm):
    class Meta:
        model = PatientVitals
        fields = ('Height_in_Centimeters','Weight_in_kilograms','Allergies','Smoker_or_not','Chronic_conditions')
