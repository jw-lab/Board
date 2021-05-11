from django.shortcuts import render
from parkingapp.models import Parking
from django.http import HttpResponseRedirect

from parkingapp.forms import ParkingForm


# Create your views here.


def parking_view(request):
    

    if request.method == 'POST':
        parking = Parking()
        
        parking_form = ParkingForm(request.POST)

        if parking_form.is_valid():
            parking.model = parking_form.cleaned_data['model']
            parking.name = parking_form.cleaned_data['name']
            parking.company = parking_form.cleaned_data['company']
            parking.plate = parking_form.cleaned_data['plate']
            parking.color = parking_form.cleaned_data['color']
            parking.lot = parking_form.cleaned_data['lot']
            parking.mobile = parking_form.cleaned_data['mobile']
            parking.save()

            return HttpResponseRedirect('/')

    else:
        parking_date = Parking.objects.last()
        parking_form = ParkingForm()
    
    context = {
        'form' : parking_form,
        'parking_date' : parking_date,
    }

    return render(request, 'parkingapp/main.html', context)