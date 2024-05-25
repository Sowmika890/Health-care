from django.db import models
from django.contrib.auth.models import User  # Add this import
from django.contrib.auth.models import User


class Provider(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    availability = models.TextField()
    operating_hours = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('booked', 'Booked'), ('cancelled', 'Cancelled')])

class Review(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

class Resource(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField()
