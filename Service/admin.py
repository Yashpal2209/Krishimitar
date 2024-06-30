from django.contrib import admin
from Service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_icon','serrvice_title','service_detail')
    
admin.site.register(Service,ServiceAdmin)
# Register your models here.
