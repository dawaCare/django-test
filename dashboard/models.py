from __future__ import unicode_literals
from django.db import models
from django.db.models import fields
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
# class Patient(models.Model):
#     Patient_name = models.CharField(max_length=60)
#     age = models.PositiveSmallIntegerField()
#     location = models.CharField(max_length=30)
#     condition = models.CharField(max_length=150)
#     medication = models.CharField(max_length=30)
#     initial_visit = models.DateField()
#     followup_appt = models.DateField()
#     reminder_freq = models.PositiveSmallIntegerField()

@python_2_unicode_compatible
class Outpatient(models.Model):
    visit_date = models.DateTimeField(blank=True)
    first_name = models.CharField('First Name', max_length=100)
    last_name = models.CharField(max_length=100)
    # age contains invalid literals for float
    age = models.CharField(max_length=50,blank=True, null=True)
    gender = models.CharField(max_length=20)
    main_phone = models.PositiveIntegerField(null=True)
    alt_phone = models.PositiveIntegerField(null=True)
    occupation = models.CharField(max_length=40)
    address = models.CharField(max_length=200)
    admitted = models.BooleanField(default=False)
    doctors_name = models.CharField(max_length=200)
    doctors_note = models.TextField(null=True)
    appt_date = models.CharField(max_length=100, blank=True, null=True)
    reminder_schedule_1_date = models.CharField(max_length=200, blank=True)
    sign_consent_for_roi = models.BooleanField(default=False)
    reason_for_not_signing_consent = models.CharField(max_length=300, blank=True)
    name_of_center = models.CharField(max_length=100, blank=True)
    patient_received_ed = models.BooleanField(default=False)
    consultation_fee = models.CharField(max_length=50, blank=True, null=True)
    admission_fee = models.IntegerField(blank=True, null=True)
    lab_fee = models.IntegerField(blank=True, null=True)
    medication_1 = models.CharField(max_length=100, blank=True)
    medication_2 = models.CharField(max_length=100, blank=True)
    medication_3 = models.CharField(max_length=100, blank=True)
    medication_4 = models.CharField(max_length=100, blank=True, null=True)
    medication_5 = models.CharField(max_length=100, blank=True, null=True)
    medication_6 = models.CharField(max_length=100, blank=True, null=True)
    medication_7 = models.CharField(max_length=100, blank=True, null=True)
    message_sent = models.TextField(blank=True)
    contacted_patient = models.BooleanField(default=False)
    patient_showed_up = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)
    sent = models.BooleanField(default=False)
    issues_with_taking_medication = models.BooleanField(default=False)
    reminder_frequency = models.CharField(max_length=300, blank=True)
    reminder_end_date = models.CharField(max_length=100, blank=True, null=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.last_name
