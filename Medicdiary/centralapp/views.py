from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from patient.models import PatientProfile
from doctor.models import DoctorProfile


def mainpage(request):
    return render(request,'centralapp/mainpage.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            # if request.user.patient.usertype=="1":
            if PatientProfile.objects.filter(patient = request.user):
                isuser = PatientProfile.objects.filter(patient = request.user)
            elif DoctorProfile.objects.filter(doctor=request.user):
                isuser = DoctorProfile.objects.filter(doctor=request.user)
            usertype = [int(each.usertype) for each in isuser][0]
            if usertype==1:
                return redirect('patient:patientProfile')
            elif usertype==2:
                return redirect('doctor:doctorProfile')
        else:
            messages.info(request,"Invalid Credentials!")
            return redirect('login')
    return render(request,'centralapp/login.html')

# uniquetogether

def About_us(request):
    return render(request,'centralapp/about_us.html')
def FAQS(request):
    return render(request,'centralapp/faqs.html')
def doc_how_to_use(request):
    return render(request,'centralapp/how_to_use_Doctor.html')
def patients_how_to_use(request):
    return render(request,'centralapp/how_to_use_User.html')
def Inside_health_records(request):
    return render(request,'centralapp/inside_health_records.html')
