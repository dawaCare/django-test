from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin
from django.contrib import admin
from dashboard.models import Outpatient

# Register your models here.

class OutpatientResource(ModelResource):

    class Meta:
        model = Outpatient

class OutpatientAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = OutpatientResource
    # list_display = ('patient_name', 'age', 'location', 'condition', 'medication', 'initial_visit', 'followup_appt', 'reminder_freq')
    list_display = ('last_name', 'first_name', 'age', 'location', 'doctors_note', 'medication_1', 'medication_2', 'medication_3', 'medication_4', 'visit_date', 'reminder_schedule_1_date', 'reminder_frequency')
    # list_display = ('visit_date', 'first_name', 'last_name', 'age', 'gender')




admin.site.register(Outpatient, OutpatientAdmin)
