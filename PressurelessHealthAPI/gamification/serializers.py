from rest_framework import serializers
from .models import *
from django.utils.translation import gettext as _
from core.serializers import *



class RequirementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Requirement
        fields = '__all__'
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )



class GoalSerializer(serializers.ModelSerializer):
    requirements = RequirementSerializer(RequirementSerializer, many = True, read_only = True)
    reached_on = serializers.SerializerMethodField()

    # reached_on = GoalHistorySerializer(read_only = True, source = "latest_history")

    def get_reached_on(self, obj: Goal):
        return obj.latest_history[0].reached_on if obj.latest_history and len(obj.latest_history) > 0 else None

    class Meta:
        model = Goal
        fields = '__all__'
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )



# class GoalRequirementSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = GoalRequirement
#         fields = '__all__'
#         # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
#         read_only_fields = ('id', )



class ChallengeSerializer(serializers.ModelSerializer):
    requirements = RequirementSerializer(many = True, read_only = True)
    latest_history = ChallengeHistorySerializer(many = True, read_only = True)

    class Meta:
        model = Challenge
        fields = '__all__'
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )



class BasicChallengeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Challenge
        exclude = ('requirements', )
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )



# class ChallengeRequirementSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = ChallengeRequirement
#         fields = '__all__'
#         # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
#         read_only_fields = ('id', )
