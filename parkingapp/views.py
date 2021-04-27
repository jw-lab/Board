from django.shortcuts import render
from parkingapp.models import Parking
from django.http import HttpResponseRedirect

# Create your views here.

def parking_view(request):
    
    if request.method == "POST":
        parking = Parking()
        parking.model = request.POST.get('model')
        parking.name = request.POST.get('name')
        parking.color = request.POST.get('color')
        parking.plate = request.POST.get('plate')
        parking.mobile = request.POST.get('mobile')
        parking.lot = request.POST.get('lot')
    
        parking.save()
        return HttpResponseRedirect('/parking')
    else:
        parking_list = Parking.objects.all()
        return render(request,'parkingapp/main.html', context={'parking_list': parking_list})