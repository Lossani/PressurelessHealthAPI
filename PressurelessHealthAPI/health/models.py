from django.db import models
from core.models import *



# Create your models here.
class Measurement(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING, null = False)
    measurement_date = models.DateTimeField(null = False)
    update_date = models.DateTimeField(auto_now = True, null = False)
    systolic_pressure = models.DecimalField(null = False, max_digits = 5, decimal_places = 2)
    diastolic_pressure = models.DecimalField(null = False, max_digits = 5, decimal_places = 2)
    heart_rate = models.IntegerField(null = True)
    temperature = models.IntegerField(null = True)
    blood_oxygen = models.IntegerField(null = True)
    # wearable = models.ForeignKey(Wearable, on_delete = models.DO_NOTHING, null = False)
