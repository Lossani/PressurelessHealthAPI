from django.db import models
from django.contrib.auth import get_user_model
from .constants import WEEKDAY
from core.models import User



# Create your models here.
class Measurement(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING, null = False)
    measurement_date = models.DateTimeField(null = False, auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True, null = False)
    systolic_pressure = models.DecimalField(null = False, max_digits = 5, decimal_places = 2)
    diastolic_pressure = models.DecimalField(null = False, max_digits = 5, decimal_places = 2)
    heart_rate = models.IntegerField(null = True)
    temperature = models.IntegerField(null = True)
    blood_oxygen = models.IntegerField(null = True)
    used_recommended_method = models.BooleanField(null = False, default = False)
    comments = models.CharField(null = False, blank = True, max_length = 1024)
    # wearable = models.ForeignKey(Wearable, on_delete = models.DO_NOTHING, null = False)



class Medication(models.Model):
    name = models.CharField(null = False, max_length = 250)
    description = models.CharField(null = True, max_length = 1024)

    user = models.ForeignKey(User, on_delete = models.DO_NOTHING, null = False)
    deleted = models.BooleanField(null = False, default = False)



class MedicationFrequency(models.Model):
    medication = models.ForeignKey(Medication, on_delete = models.DO_NOTHING, null = False)
    # weekday = models.PositiveIntegerField(choices = WEEKDAY.choices, null = False)
    hour = models.CharField(null = False, max_length = 50)
    dose = models.CharField(null = False, max_length = 250)
    deleted = models.BooleanField(null = False, default = False)
    monday = models.BooleanField(null = False, default = False)
    tuesday = models.BooleanField(null = False, default = False)
    wednesday = models.BooleanField(null = False, default = False)
    thursday = models.BooleanField(null = False, default = False)
    friday = models.BooleanField(null = False, default = False)
    saturday = models.BooleanField(null = False, default = False)
    sunday = models.BooleanField(null = False, default = False)



class Article(models.Model):
    title = models.CharField(null = False, max_length = 250)
    content = models.CharField(null = True, max_length = 1024)

    enabled = models.BooleanField(null = False, default = True)
