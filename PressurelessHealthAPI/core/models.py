from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager
from gamification.models import *
from datetime import datetime
from django.utils import timezone as dtz

# Create your models here.



class User(AbstractUser):
    """
    Model User personalizado para el proyecto.
    """

    phone = models.CharField(null = True, max_length = 50)

    age = models.PositiveIntegerField(null = True, default = None)
    weight = models.PositiveIntegerField(null = True, default = None)
    country = models.CharField(null = True, default = "Peru", max_length = 50)
    gender = models.CharField(null = False, default = "Unspecified", max_length = 50)
    points = models.PositiveIntegerField(null = False, default = 0)
    avatar_url = models.CharField(null = False, max_length = 255)
    email = models.EmailField(unique = True, null = False)
    password_reset_code = models.CharField(null = True, max_length = 7)
    password_reset_code_last_request = models.DateTimeField(null = True, default = None)

    # fechaCreacion = models.DateTimeField(auto_now_add = True, null = False)
    # fechaEdicion = models.DateTimeField(auto_now = True, null = False)
    # ipCreacion = models.CharField(max_length = 40, null = True)
    # ipEdicion = models.CharField(max_length = 40, null = True)
    # usuarioCreacion = models.ForeignKey('self', on_delete = models.DO_NOTHING, related_name = "tm_usuario_usuario_creacion", null = True)
    # usuarioEdicion = models.ForeignKey('self', on_delete = models.DO_NOTHING, related_name = "tm_usuario_usuario_edicion", null = True)

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['-pk']



class Contact(models.Model):
    first_name = models.CharField(null = False, max_length = 50)
    last_name = models.CharField(null = True, max_length = 50)
    email = models.CharField(null = True, max_length = 50)
    phone = models.CharField(null = False, max_length = 50)
    address = models.CharField(null = True, max_length = 50)
    relationship = models.CharField(null = True, max_length = 50)

    user = models.ForeignKey(User, on_delete = models.DO_NOTHING, null = False)

    deleted = models.BooleanField(null = False, default = False)



class GoalHistory(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING, null = False)
    goal = models.ForeignKey(Goal, on_delete = models.DO_NOTHING, null = False)
    reached_on = models.DateTimeField(null = False)



class ChallengeHistory(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING, null = False)
    challenge = models.ForeignKey(Challenge, on_delete = models.DO_NOTHING, null = False)
    start_date = models.DateTimeField(null = False, default = dtz.now)
    end_date = models.DateTimeField(null = True)
    succeeded = models.BooleanField(null = False, default = False)



from health.models import MedicationFrequency



class Reminder(models.Model):
    medication_frequency = models.OneToOneField(MedicationFrequency, on_delete = models.CASCADE, null = False, primary_key = False)
    active = models.BooleanField(null = False, default = True)
    triggered_times = models.PositiveIntegerField(null = False, default = 0)



class NotificationHistory(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING, null = False)
    body = models.CharField(null = True, max_length = 50)
    send_date = models.DateTimeField(null = False)
    reminder = models.ForeignKey(Reminder, on_delete = models.DO_NOTHING, null = True)



class DebugLog(models.Model):
    text = models.TextField(null = False, blank = False)
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING, null = True, blank = True)
