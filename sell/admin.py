from django.contrib import admin
from sell.models import Sell
# Register your models here.
class SellAdmin(admin.ModelAdmin):
    list_display=('item_img','item_title','item_detail','item_date','item_quant','item_price')

admin.site.register(Sell,SellAdmin)