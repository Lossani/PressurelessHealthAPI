from rest_framework import serializers

from gamification.functions import *
from .models import *
from django.utils.translation import gettext as _
from gamification.serializers import *



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('password', 'is_superuser', 'is_staff', 'groups', 'user_permissions')
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )



class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )



class MedicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medication
        fields = '__all__'
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )



class MedicationFrequencySerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicationFrequency
        fields = '__all__'
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )



class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reminder
        fields = '__all__'
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )



class GoalHistorySerializer(serializers.ModelSerializer):
    goal = GoalSerializer(read_only = True)
    class Meta:
        model = GoalHistory
        fields = '__all__'
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )



class ChallengeHistorySerializer(serializers.ModelSerializer):
    challenge = ChallengeSerializer(read_only = True)
    progress = serializers.SerializerMethodField()
    
    def get_progress(self, obj: ChallengeHistory):
        if obj.succeeded:
            return 100
        return calculate_challenge_met_requirements_count(obj.user_id, obj.challenge, obj) / obj.challenge.requirements.count() * 100
    
    
    class Meta:
        model = ChallengeHistory
        fields = '__all__'
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )



class NotificationHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = NotificationHistory
        fields = '__all__'
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )
