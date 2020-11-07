from . import views
from django.urls import path

app_name = 'centralapp'
urlpatterns = [

    path('',views.mainpage,name='mainpage'),
    path('FAQS/',views.FAQS,name ='FAQS'),
    path('medical_practitioners/How_to_use',views.doc_how_to_use,name ='doc_how_to_use'),
    path('friends-and-family/How_to_use',views.patients_how_to_use,name ='patients_how_to_use'),
    path('Inside_health_records/',views.Inside_health_records,name ='Inside_health_records'),
    path('login/',views.login,name='login'),
]
