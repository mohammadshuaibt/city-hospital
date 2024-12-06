from django.urls import path,include
from django.shortcuts import render
from . import views

urlpatterns = [
    path('',views.mainPage, name = 'index'),
    path('doctors/',views.doctorsPage,name = 'doctors'),
    path('booking/',views.bookingPage,name = 'booking'),
    path('about/',views.aboutPage,name = 'about'),
    path('contact/',views.contactPage,name='contact'),
    path('department/',views.departmentPage,name = 'department')
]