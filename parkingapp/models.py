from django.db import models
from django.urls import reverse

# Create your models here.

class Parking(models.Model):
    id = models.AutoField(primary_key= True)
    model = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=50,null=True)
    company = models.CharField(max_length=50,null=True)
    color = models.CharField(max_length=50,null=True)
    plate = models.CharField(max_length=50, null=True)
    mobile = models.CharField(max_length=13, null=True)
    lot = models.CharField(max_length=50, null=True)
    date = models.DateTimeField(auto_now_add=True)
