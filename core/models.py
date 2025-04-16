from django.db import models

# Create your models here.
class Crop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()

class WeatherInfo(models.Model):
    date = models.DateField(auto_now_add=True)
    temperature = models.FloatField()
    condition = models.CharField(max_length=100)