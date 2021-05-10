from django.urls import path
from parkingapp.views import ParkingCreateView

app_name = 'parkingapp'

urlpatterns = [
    path('',ParkingCreateView.as_view(), name='ParkingCreateView'),
]