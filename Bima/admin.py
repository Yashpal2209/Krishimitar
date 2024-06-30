from django.contrib import admin
from Bima.models import Bima
# Register your models here.
class BimaAdmin(admin.ModelAdmin):
    list_display=('user_name','size','rno','income','income','type','cropname')

admin.site.register(Bima,BimaAdmin)