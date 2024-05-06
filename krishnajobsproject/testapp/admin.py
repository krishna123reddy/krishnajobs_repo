from django.contrib import admin
from testapp.models import HydJobs
class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['id','date','qcompany','title','address','email','phonenumber']
admin.site.register(HydJobs,HydJobsAdmin)
# Register your models here.
