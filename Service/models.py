from django.db import models

# Create your models here.
class Service(models.Model):
    service_icon=models.CharField(max_length=50)
    serrvice_title=models.CharField(max_length=50)
    service_detail=models.TextField(max_length=200)