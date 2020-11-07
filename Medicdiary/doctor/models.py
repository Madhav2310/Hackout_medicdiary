from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from patient.models import PatientProfile

class DoctorProfile(models.Model):

    doctor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete= models.CASCADE)
    name = models.CharField(max_length=30, blank=False)
    Gender = models.CharField(max_length=30)
    Specialisation = models.CharField(max_length=30)
    phone = models.CharField(max_length=40, blank=False, help_text='10 digit Mobile Number')
    City = models.CharField(max_length=30)
    Registration_Number = models.CharField(max_length=40, blank=False)
    Registration_Council = models.CharField(max_length=100, blank=False)
    Registration_year = models.IntegerField(blank=False)
    Degree = models.CharField(max_length=100, blank=False)
    College = models.CharField(max_length=100, blank=False)
    Year_of_completion = models.IntegerField()
    Profile_pic = models.ImageField(default = 'doctors_profile_pictures/defaultprofilepic.jpg', upload_to = 'doctors_profile_pictures')
    Medical_registration_proof = models.FileField(upload_to = 'DoctorRegProofs',blank = True)
    Current_place_of_work = models.CharField(max_length=30)
    Aadhar_Number= models.IntegerField(blank=False, help_text='12 digit unique Aadhar Number')
    usertype = models.IntegerField(default = 2)
    # mypatients = models.ManyToManyField(PatientProfile,through = "pats", related_name = "mypat")
    # mypatient = models.ManyToManyField(PatientProfile, related_name = "mypat")

    def __str__(self):
        return self.name
