from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.department)
admin.site.register(models.doctor)
admin.site.register(models.Received_Contact)
@admin.register(models.bookk)
class BookkAdmin(admin.ModelAdmin):
    readonly_fields = ['booked_on']  # Make booked_on read-only in the admin panel
    list_display = ['patient_name', 'doctor_name', 'booking_date', 'booked_on']  # Display booked_on in the list view