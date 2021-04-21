from django.db import models

# Create your models here.

class Weather(models.Model):
    value=models.CharField(max_length=250)

class Place(models.Model):
    name=models.CharField(max_length=250)
    description=models.TextField()
    weather=models.ManyToManyField(Weather)

class TravelDate(models.Model):
    startDate=models.DateTimeField()
    endDate=models.DateTimeField()
    place=models.ForeignKey(Place,on_delete=models.CASCADE)