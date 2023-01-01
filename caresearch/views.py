from django.shortcuts import render
from django.views import generic
from .models import Careprovider, Careseeker

class CareproviderList(generic.ListView):
    model = Careprovider
    queryset = Careprovider.objects.order_by('address_line3')
    template_name = 'index.html'
    paginate_by = 6
