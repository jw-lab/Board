from django import forms
from .models import Parking

class ParkingForm(ModelForm):
    class Meta:
        model = Parking
        fields = '__all__'
