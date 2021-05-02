from django.urls import path
from parkingapp.views import parking_view

app_name = 'parkingapp'

urlpatterns = [
    path('',parking_view, name='parking_view'),
]