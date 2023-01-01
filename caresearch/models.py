from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Model for Care Seeker

class Careseeker(models.Model):
    careseeker_username	= models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50)
    address_line3 = models.CharField(max_length=50)
    county = models.CharField(max_length=25)
    postcode = models.CharField(max_length=6)
    home_phone_number = models.IntegerField()
    mobile_phone_number = models.IntegerField()
    email_address = models.CharField(max_length=50)
    needs_assistance = models.BooleanField(default=False)
    needs_disabled_space = models.BooleanField(default=False) 

def __str__(self):
    return self.title

class Careprovider(models.Model):
    provider_username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    business_name = models.CharField(max_length=35)
    main_contact_name = models.CharField(max_length=35)
    address_line1 = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50)
    address_line3 = models.CharField(max_length=50)
    postcode = models.CharField(max_length=8)
    phone_number = models.IntegerField()
    out_of_hours_phone_number = models.IntegerField()
    email_address = models.CharField(max_length=50)
    has_disabled_space = models.BooleanField() 
    careprovider_image = CloudinaryField('image', default='placeholder')
    

class Rating(models.Model):
    ratings_id = models.ForeignKey(Careprovider, on_delete=models.CASCADE, related_name='ratings')
    Rating_number = models.IntegerField()
    title = models.CharField(max_length=35)
    comment = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_created']