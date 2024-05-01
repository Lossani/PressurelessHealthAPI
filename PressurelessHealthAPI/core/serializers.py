from rest_framework import serializers

from gamification.functions import *
from .models import *



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
        # fields = '__all__'
        exclude = ('user', )
        read_only_fields = (
            'id',
            'user',
        )
        extra_kwargs = { 'user': { 'required': False } }
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )



class BasicReminderSerializer(serializers.ModelSerializer):
    medication_frequency_id = serializers.IntegerField()

    class Meta:
        model = Reminder
        # fields = '__all__'
        exclude = ('medication_frequency', )
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )



from health.serializers import BasicMedicationFrequencySerializer



class DetailedReminderSerializer(serializers.ModelSerializer):
    medication_frequency = BasicMedicationFrequencySerializer()

    class Meta:
        model = Reminder
        fields = '__all__'
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )



class GoalHistorySerializer(serializers.ModelSerializer):
    # goal = GoalSerializer(read_only = True)
    # goal_id = serializers.PrimaryKeyRelatedField(queryset = Goal.objects, source = 'goal')

    class Meta:
        model = GoalHistory
        fields = '__all__'
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )



class ChallengeHistorySerializer(serializers.ModelSerializer):
    # challenge = ChallengeSerializer(read_only = True)
    # challenge_id = serializers.PrimaryKeyRelatedField(queryset = Challenge.objects, source = 'challenge')
    progress = serializers.SerializerMethodField()

    # user = serializers.ModelField(ChallengeHistory.user, required = False, read_only = True)
    # user_id = serializers.ModelField(ChallengeHistory.user_id, required = False, read_only = True)

    def get_progress(self, obj: ChallengeHistory):
        if obj.succeeded:
            return 100
        return calculate_challenge_met_requirements_percent(obj.user_id, obj.challenge, obj) / obj.challenge.requirements.count() * 100

    class Meta:
        model = ChallengeHistory
        # fields = '__all__'
        exclude = ('user', )
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = (
            'id',
            'user',
            'start_date',
        )
        extra_kwargs = { 'user': { 'required': False } }



class NotificationHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = NotificationHistory
        fields = '__all__'
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )
