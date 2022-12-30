from django.contrib import admin
from .models import Careseeker, Careprovider, Rating

admin.site.register(Careseeker)

admin.site.register(Careprovider)

admin.site.register(Rating)
