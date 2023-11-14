from rest_framework import serializers
from .models import *
from django.utils.translation import gettext as _



class RequirementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Requirement
        fields = '__all__'
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )



class GoalSerializer(serializers.ModelSerializer):
    # requirements = RequirementSerializer(many = True, read_only = True, source = 'requirement_set')
    
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
    
    class Meta:
        model = Challenge
        fields = '__all__'
        # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
        read_only_fields = ('id', )



# class ChallengeRequirementSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = ChallengeRequirement
#         fields = '__all__'
#         # exclude = ('fechaCreacion', 'fechaEdicion', 'usuarioCreacion', 'usuarioEdicion', 'ipCreacion', 'ipEdicion')
#         read_only_fields = ('id', )
