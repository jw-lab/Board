from django.db import models

# Create your models here.

class Parking(models.Model):
    model = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=50,null=True)
    company = models.CharField(max_length=50,null=True)
    color = models.CharField(max_length=50,null=True)
    plate = models.CharField(max_length=50,null=True)
    mobile = models.IntegerField(null=True)
    lot = models.CharField(max_length=50,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
