from django import forms
from django.forms import ModelForm
from .models import Parking


class ParkingForm(ModelForm):
    class Meta:
        model = Parking
        fields = ['model','name','company','color','plate','mobile','lot']

        COLOR_CHOICES = (
            ('','Please Select the color of your car'),
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

        widgets = {
            'model' : forms.TextInput(attrs={'placeholder': 'Please enter your car model'} ),
            'name' : forms.TextInput(attrs={'placeholder': 'Please enter your name'} ),
            'company' : forms.TextInput(attrs={'placeholder': 'Please enter your company'} ),
            'plate' : forms.TextInput(attrs={'placeholder': 'Please enter your car plate'} ),
            'mobile' : forms.TextInput(attrs={'placeholder': '010-1234-5678', 'id': 'numbers'}),
            'lot' : forms.TextInput(attrs={'placeholder': 'Please enter your parking lot'} ),
            'color' : forms.Select(choices=COLOR_CHOICES, attrs={'onchange' : "colorChange(this.value);"})
        }
