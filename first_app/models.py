from django.db import models
from django.core.exceptions import ValidationError
import re

# Create your models here.
class department(models.Model):
    dept_name = models.CharField(max_length=100)
    dep_description = models.TextField()
    dep_image = models.FileField(upload_to='departments/',default='default.jpg')

    def __str__(self):
        return self.dept_name
    

class doctor(models.Model):
    doctor_name = models.CharField(max_length = 40)
    doc_spec = models.TextField()
    dept_name = models.ForeignKey(department,on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors/')

    def __str__(self):
        return self.doctor_name
    

###contact page starts below

def validate_indian_phone_number(value):
        pattern = r'^(\+91[\-\s]?)?[6-9]\d{9}$'
        if not re.match(pattern, value):
            raise ValidationError("Enter a valid Indian mobile number.")
    
class Received_Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=254)
    phone_number = models.CharField(
        max_length=13,  # +91 9876543210 = 13 characters
        validators=[validate_indian_phone_number],
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

#booking 
class bookk(models.Model):
    patient_name = models.CharField(max_length=150)
    patient_number = models.CharField(max_length=10,validators=[validate_indian_phone_number])
    patient_email = models.EmailField()
    doctor_name = models.ForeignKey(doctor,on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now = True)

    def __str__(self):
        return self.patient_name