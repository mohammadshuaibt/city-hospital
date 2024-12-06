from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import department,doctor,Received_Contact
from .forms import receivedcontactform,bookkform
# Create your views here.
def mainPage(request):
    return render(request,'index.html') 

def doctorsPage(request):
    doctor_info = doctor.objects.all()
    return render(request,'doctors.html',{'doctor_info':doctor_info})

def bookingPage(request):
    if request.method == 'POST':
        form = bookkform(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('booking')
    else:
        form = bookkform()
    return render(request,'booking.html',{'form': form})

def aboutPage(request):
    return render(request,'about.html')

def contactPage(request):
    if request.method == 'POST':
        form = receivedcontactform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = receivedcontactform()
    return render(request,'contact.html',{'form': form})

def departmentPage(request):
    department_info = department.objects.all()
    return render(request,'department.html',{'department_info':department_info})

