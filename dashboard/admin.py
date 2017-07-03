from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin
from django.contrib import admin
from dashboard.models import Outpatient

# Register your models here.

class OutpatientResource(ModelResource):

    class Meta:
        model = Outpatient

class OutpatientAdmin(admin.ModelAdmin):
    resource_class = OutpatientResource
    # list_display = ('Patient_name', 'age', 'location', 'condition', 'medication', 'initial_visit', 'followup_appt', 'reminder_freq')
    # list_display = ('visit_date', 'first_name', 'last_name', 'age', 'gender')




admin.site.register(Outpatient, OutpatientAdmin)
