from django import forms
from .models import Received_Contact,bookk

class receivedcontactform(forms.ModelForm):
    class Meta:
        model = Received_Contact
        fields = ['first_name', 'last_name','email_address','phone_number']

class bookkform(forms.ModelForm):
    class Meta:
        model = bookk
        fields = ['patient_name','patient_number','patient_email','doctor_name','booking_date']