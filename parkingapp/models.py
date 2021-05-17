from django.db import models
from django.urls import reverse
from django import forms
# Create your models here.

class Parking(models.Model):
    id = models.AutoField(primary_key= True)
    model = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    plate = models.CharField(max_length=50)
    mobile = models.CharField(max_length=13)
    lot = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
