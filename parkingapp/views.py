from django.shortcuts import render
from parkingapp.models import Parking
from django.http import HttpResponseRedirect
from django.views.generic import CreateView

# Create your views here.

# def parking_view(request):
    
#     if request.method == "POST":
#         parking = Parking()
#         parking.model = request.POST.get('model')
#         parking.name = request.POST.get('name')
#         parking.company = request.POST.get('company')
#         parking.color = request.POST.get('color')
#         parking.plate = request.POST.get('plate')
#         parking.mobile = request.POST.get('mobile')
#         parking.lot = request.POST.get('lot')

#         parking.save()
#         return HttpResponseRedirect('/')
#     else:
#         parking_list = Parking.objects.all()
#         return render(request,'parkingapp/main.html', context={'parking_list': parking_list})

class ParkingCreateView(CreateView):
    model = Parking
    fields = '__all__'
    success_url = '/'
    template_name = 'parkingapp/main.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(ParkingCreateView, self).get_form(form_class)
        form.fields['model'].widget.attrs ={'placeholder': 'Please enter your car model'}
        form.fields['name'].widget.attrs ={'placeholder': 'Please enter your name'}
        form.fields['company'].widget.attrs ={'placeholder': 'Please enter your car brand'}
        form.fields['plate'].widget.attrs ={'placeholder': 'Please enter your car number'}
        form.fields['mobile'].widget.attrs ={'placeholder': 'Please enter your phone number'}
        form.fields['lot'].widget.attrs ={'placeholder': 'Please enter where you want to park'}
        return form