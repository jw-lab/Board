from django.shortcuts import render
from parkingapp.models import Parking
from django.http import HttpResponseRedirect

from parkingapp.forms import ParkingForm


# Create your views here.


def parking_view(request):
    if request.method == 'POST':
        form = ParkingForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        parking_date = Parking.objects.last()
        form = ParkingForm()
    
    context = {
        'form' : form,
        'parking_date' : parking_date,
    }

    return render(request, 'parkingapp/main.html', context)