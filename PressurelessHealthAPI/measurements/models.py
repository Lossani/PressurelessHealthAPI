from django.db import models
from users.models import *

# Create your models here.
class Measurement(models.Model):
    idMeasurement = models.AutoField(primary_key = True)
    idUser = models.ForeignKey(User, on_delete = models.DO_NOTHING, null = False)
    creationDate = models.DateTimeField(auto_now_add = True, null = False)
    updatedate = models.DateTimeField(auto_now = True, null = False)
    systolicPressure = models.DecimalField(null = False, max_digits = 3, decimal_places = 2)
    diastolicPressure = models.DecimalField(null = False, max_digits = 3, decimal_places = 2)
    heartRate = models.IntegerField(null = True)
    temperature = models.IntegerField(null = True)
    bloodOxygen = models.IntegerField(null = True)
    # wearable = models.ForeignKey(Wearable, on_delete = models.DO_NOTHING, null = False)
    