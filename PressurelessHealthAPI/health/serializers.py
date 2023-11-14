from rest_framework import serializers
from .models import *
from django.utils.translation import gettext as _



class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = '__all__'
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )