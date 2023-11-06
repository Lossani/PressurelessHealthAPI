from django.db import models
from django.contrib.auth.models import AbstractUser

from users.managers import CustomUserManager

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