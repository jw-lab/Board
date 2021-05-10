from django.db import models
from django.urls import reverse

# Create your models here.

class Parking(models.Model):
    model = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=50,null=True)
    company = models.CharField(max_length=50,null=True)

    COLOR_SELECT = (
        ('white', 'white'),
        ('black', 'black'),
        ('gray', 'gray'),
        ('silver', 'silver'),
        ('red', 'red'),
        ('blue', 'blue'),
        ('green', 'green'),
        ('gold', 'gold'),
        ('brown', 'brown'),
        ('orange', 'orange'),
    )

    color =  models.CharField(
        max_length=6,
        choices=COLOR_SELECT,
        blank=True,
        default='',
    )


    plate = models.CharField(max_length=50, null=True)
    mobile = models.CharField(max_length=13, null=True)
    lot = models.CharField(max_length=50, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
