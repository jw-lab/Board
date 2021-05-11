from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
    list_display = ('id','model','name','company','color','plate','mobile','lot','date')


