
from django.db import models

class BMCProfile(models.Model):
    panchayat_name = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    block = models.CharField(max_length=200)
    population = models.IntegerField()

    def __str__(self):
        return self.panchayat_name
