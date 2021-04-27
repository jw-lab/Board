from django.db import models

# Create your models here.

class Parking(models.Model):
    model = models.CharField(max_length=50,null=False)
    name = models.CharField(max_length=50,null=False)
    color = models.CharField(max_length=50,null=False)
    plate = models.CharField(max_length=50,null=False)
    mobile = models.CharField(max_length=50,null=False)
    lot = models.CharField(max_length=50,null=False)