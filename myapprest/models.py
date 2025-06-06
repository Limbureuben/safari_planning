from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#organization staff anafanya registration ya organizations kwa hizi inputs
class Organizations(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('suspended', 'Suspended'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organizations')
    organization_name = models.CharField(max_length=255)
    discriptions = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='company_images')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')


#Organization staff anafanya registration ya package kwa hizi input
class PackageRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='packages')
    package_name = models.CharField(max_length=255)
    discriptions = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    price = models.CharField(max_length=255)



#user atafanya booking ya package husika
class BookingPackage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number= models.CharField(max_length=255)
    start_date = models.DateField()
    participant_number = models.CharField(max_length=255)
    special_requirements = models.CharField(max_length=255)