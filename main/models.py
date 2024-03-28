from django.db import models

class Countries(models.Model):
    name = models.CharField(max_length=60, unique = True, blank = True)
    capital = models.CharField(max_length=60, unique = True, blank = True)
    subregion = models.CharField(max_length=60, blank = True)
    region = models.CharField(max_length=60, blank = True)
    population = models.BigIntegerField(blank = True)
    area = models.BigIntegerField(blank = True)
    imezones = models.JSONField(blank = True)
    borders = models.JSONField(blank = True)
    numericCode = models.CharField(max_length=60, unique = True, blank = True)
    flag = models.CharField(max_length=60, unique = True, blank = True)
# Create your models here.
