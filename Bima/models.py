from django.db import models
from django.forms import DecimalField

# Create your models here.
class Bima(models.Model):
    user_name=models.CharField(max_length=30,default="lenovo")
    size=models.DecimalField(max_digits=10, decimal_places=2)
    rno=models.IntegerField()
    income=models.DecimalField(max_digits=10, decimal_places=2)
    type=models.CharField(max_length=10)
    cropname=models.CharField(max_length=30)

