from rest_framework import serializers
from rest_framework.response import Response

from .models import *
from core.serializers import BasicReminderSerializer
from core.models import Reminder



class MeasurementSerializer(serializers.ModelSerializer):
    measurement_date = serializers.DateTimeField(format = "%Y-%m-%dT%H:%M:%S", required = False, read_only = True)

    class Meta:
        model = Measurement
        # fields = '__all__'
        exclude = ('user', )
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = (
            'id',
            'user',
            'measurement_date',
        )
        extra_kwargs = { 'user': { 'required': False } }



class BasicMedicationFrequencySerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicationFrequency
        depth = 1
        fields = '__all__'
        read_only_fields = ('id', )



class MedicationFrequencySerializer(serializers.ModelSerializer):
    reminder = BasicReminderSerializer(required = False, read_only = True)
    medication_id = serializers.IntegerField()

    def create(self, validated_data):
        frequency = MedicationFrequency.objects.create(**validated_data)
        if self.initial_data.get('reminder_notification_enabled', False):
            Reminder.objects.create(active = True, medication_frequency_id = frequency.pk)
            frequency.reminder

        return frequency

    def update(self, instance, validated_data):
        super().update(instance, validated_data)

        reminder, created = Reminder.objects.update_or_create(
            medication_frequency_id = instance.pk,
            defaults = {
                'active': self.initial_data.get('reminder_notification_enabled', False),
            },
        )
        
        instance.reminder = reminder
        
        return instance

    class Meta:
        model = MedicationFrequency
        fields = '__all__'
        depth = 1
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', 'reminder')
        extra_kwargs = {
            'monday': {
                'required': False
            },
            'tuesday': {
                'required': False
            },
            'wednesday': {
                'required': False
            },
            'thursday': {
                'required': False
            },
            'friday': {
                'required': False
            },
            'saturday': {
                'required': False
            },
            'sunday': {
                'required': False
            },
        }



class MedicationSerializer(serializers.ModelSerializer):
    frequencies = MedicationFrequencySerializer(many = True, source = 'medication_frequencies', read_only = True)

    class Meta:
        model = Medication
        # fields = '__all__'
        exclude = ('user', )
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = (
            'id',
            'user',
            'measurement_date',
        )
        extra_kwargs = { 'user': { 'required': False } }



class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )
