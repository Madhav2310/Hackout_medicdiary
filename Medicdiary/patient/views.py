from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import PatientRegisterForm,PatientProfileForm,PatientVitalsForm
from django.contrib.auth.decorators import login_required
from .models import PatientProfile,PatientVitals
from django.contrib.auth import logout

def patientRegister(request):
    if request.method =='POST':
        form = PatientRegisterForm(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.usertype= 1
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('patient:create_patientprofile')
    else:
        form = PatientRegisterForm()
    return render(request,'patient/patientregister.html',{'form':form})


@login_required
def create_patientprofile(request):
    if request.method =='POST':
        form = PatientProfileForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.save()
            return redirect('patient:patientvitals_input')
    else:
        form = PatientProfileForm()
    return render(request,'patient/patient-profile-create.html',{'form':form})

@login_required
def patientvitals_input(request):
    if request.method =='POST':
        form = PatientVitalsForm(request.POST)
        if form.is_valid():
            patientv = form.save(commit=False)
            patientv.patientv = request.user
            patientv.save()
            return redirect('patient:patientProfile')
    else:
        form = PatientVitalsForm()
    return render(request,'patient/patientvital_info.html',{'form':form})


@login_required
def patientProfile(request):
    profile = PatientProfile.objects.get(patient=request.user)
    return render(request, 'patient/patient_profile.html',{'profile':profile})

@login_required
def patientRecords(request):
    vitals = PatientVitals.objects.get(patientv=request.user)
    return render(request, 'patient/patient_records.html',{'vitals':vitals})

@login_required
def labreports(request):
    return render(request, 'patient/labreports.html')

@login_required
def medications(request):
    return render(request, 'patient/medications.html')

@login_required
def editPatient(request):
    patient = get_object_or_404(PatientProfile, patient=request.user)
    form = PatientProfileForm(request.POST, request.FILES, instance=patient)
    if form.is_valid():
        patient = form.save(commit=False)
        patient.patient = request.user
        patient.save()
        return redirect('patient:patientProfile')

    return render(request,'patient/patient-profile-edit.html',{'form':form})

@login_required
def editPatientVitals(request):
    patientv = get_object_or_404(PatientVitals, patientv=request.user)
    form = PatientVitalsForm(request.POST, request.FILES, instance=patientv)
    if form.is_valid():
        patientv = form.save(commit=False)
        patientv.patientv = request.user
        patientv.save()
        return redirect('patient:patientRecords')
    # else:
        # form = PatientVitalsForm()
    return render(request,'patient/patient-vitals-edit.html',{'form':form})
