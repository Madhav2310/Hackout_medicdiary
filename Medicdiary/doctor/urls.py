from . import views
from django.urls import path
from django.contrib.auth import views as authentication_views

app_name = 'doctor'
urlpatterns = [
    path('doctorProfile/', views.doctorProfile, name='doctorProfile'),
    path('createDoctorProfile/',views.create_doctorprofile,name ='create_doctorprofile'),
    path('doctorRegister/',views.doctorRegister,name = 'doctorRegister'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='centralapp/logout.html'), name='logout'),
]
