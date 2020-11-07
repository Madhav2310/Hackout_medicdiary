from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from doctor.models import *





class PatientProfile(models.Model):


    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    patient = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete= models.CASCADE)
    name = models.CharField(max_length=30, blank=False)
    age = models.IntegerField(blank=False)
    address = models.TextField(max_length=500, blank=False)
    phone = models.CharField(max_length=40, blank=False, help_text='10 digit Mobile Number')
    emergency_contact = models.CharField(max_length=40, blank=False)
    profession = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    profile_pic = models.ImageField(default = 'patients_profile_pictures/defaultprofilepic.jpg', upload_to = 'patients_profile_pictures')
    Aadhar_Number= models.IntegerField(blank=False, help_text='12 digit unique Aadhar Number')
    usertype = models.IntegerField(default = 1)
    # AccessCode = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class PatientVitals(models.Model):
    patientv = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Height_in_Centimeters = models.CharField(max_length=100, blank=False, help_text='Height in centimeters')
    Weight_in_kilograms = models.CharField(max_length=100, blank=False, help_text='Weight in kilograms')
    Allergies = models.TextField(max_length=30)
    Smoker_or_not = models.CharField(max_length=30)
    Chronic_conditions = models.CharField(max_length=30, help_text='Your current long term diseases. <br>Ex. High BP, Diabetes etc')

class LabReports(models.Model):
    patientl = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    report_name = models.CharField(max_length=100, blank=False)
    report_date = models.DateField()
    upload_date = models.DateField(auto_now=True)
    labreportfile = models.FileField(upload_to = 'PatientLabReports')
