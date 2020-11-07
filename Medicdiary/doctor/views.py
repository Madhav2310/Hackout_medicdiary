from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import DoctorRegisterForm, DoctorProfileForm
from django.contrib.auth.decorators import login_required
from .models import DoctorProfile
from django.views import View


def doctorRegister(request):
    if request.method =='POST':
        form = DoctorRegisterForm(request.POST)
        if form.is_valid():
            # form.save()
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            # return redirect('login')
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('doctor:create_doctorprofile')
    else:
        form = DoctorRegisterForm()
    return render(request,'doctor/doctorRegister.html',{'form':form})

@login_required
def create_doctorprofile(request):
    if request.method =='POST':
        form = DoctorProfileForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.doctor = request.user
            doctor.save()
            # form.doctor = request.user
            # form.save()
            return redirect('doctor:doctorProfile')
    else:
        form = DoctorProfileForm()
    return render(request,'doctor/doctor-profile-create.html',{'form':form})


@login_required
def doctorProfile(request):
    profile = DoctorProfile.objects.get(doctor=request.user)
    return render(request, 'doctor/doctor_profile.html',{'profile':profile})
