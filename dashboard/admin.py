from django.contrib import admin
from dashboard.models import Outpatient
# Register your models here.

class OutpatientAdmin(admin.ModelAdmin):
    list_display = ('visit_date', 'first_name', 'last_name', 'age', 'gender')

admin.site.register(Patient, OutpatientAdmin)
