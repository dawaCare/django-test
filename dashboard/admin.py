from django.contrib import admin
from dashboard.models import Outpatient
# Register your models here.

class OutpatientAdmin(admin.ModelAdmin):
    # list_display = ('Patient_name', 'age', 'location', 'condition', 'medication', 'initial_visit', 'followup_appt', 'reminder_freq')
    list_display = ('visit_date', 'first_name', 'last_name', 'age', 'gender')

admin.site.register(Outpatient, OutpatientAdmin)
