from django.db import models
from django.utils import timezone

# Create your models here.
class Pet(models.Model):
    breed = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=30, default="Dog")
    owner_id = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)

class Location(models.Model):
    pet_id = models.IntegerField()
    user_id = models.IntegerField()
    address = models.CharField(max_length=100)
    lat = models.FloatField()
    long = models.FloatField()