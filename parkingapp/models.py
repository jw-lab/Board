from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Parking(models.Model):
    model = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=50,null=True)
    company = models.CharField(max_length=50,null=True,default='')
    color = models.CharField(max_length=50,null=True)
    plate = models.CharField(max_length=50,null=True)
    mobile = PhoneNumberField()
    lot = models.CharField(max_length=50,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)