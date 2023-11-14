from .serializers import *
from .models import *
from rest_framework import viewsets
from .views import *


class RequirementViewSet(viewsets.ModelViewSet):
    allowed_filter_params = []

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer
    http_method_names = [ 'get', 'post']



class GoalViewSet(viewsets.ModelViewSet):
    allowed_filter_params = []
    
    def list(self, request, *args, **kwargs):
        calculate_requirements(User.objects.get(pk = 2))
        return super().list(request, *args, **kwargs)

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    http_method_names = [ 'get', 'post']



# class GoalRequirementViewSet(viewsets.ModelViewSet):
#     allowed_filter_params = []

#     # authentication_classes = (TokenAuthentication,)
#     # permission_classes = (IsAuthenticated,)
#     queryset = GoalRequirement.objects.all()
#     serializer_class = GoalRequirementSerializer
#     http_method_names = [ 'get', 'post']



class ChallengeViewSet(viewsets.ModelViewSet):
    allowed_filter_params = []

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    http_method_names = [ 'get', 'post']



# class ChallengeRequirementViewSet(viewsets.ModelViewSet):
#     allowed_filter_params = []

#     # authentication_classes = (TokenAuthentication,)
#     # permission_classes = (IsAuthenticated,)
#     queryset = ChallengeRequirement.objects.all()
#     serializer_class = ChallengeRequirementSerializer
#     http_method_names = [ 'get', 'post']