from django.db import models

# Create your models here.
class Sell(models.Model):
    user_name=models.CharField(max_length=30,default="lenovo")
    item_img=models.ImageField()
    item_title=models.CharField(max_length=50)
    item_detail=models.TextField()
    item_date=models.DateField()
    item_quant=models.IntegerField(default=0)
    item_price=models.DecimalField(max_digits=10, decimal_places=2)
