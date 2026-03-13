from django.db import models

# Create your models here.
class Airport(models.Model):
    code=models.CharField(max_length=3)
    city=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"
    

class Flights(models.Model):
    origin=models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination=models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.origin} to {self.destination}"
    
from django.contrib.auth.models import User

class Passenger(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    flights = models.ManyToManyField(Flights, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
