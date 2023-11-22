from PressurelessHealthAPI.api import ListFilterViewSet
from .serializers import *
from .models import *
from rest_framework import viewsets
from .views import *
from .functions import *


class RequirementViewSet(ListFilterViewSet):
    allowed_filter_params = []

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer
    http_method_names = [ 'get', 'post']



class GoalViewSet(ListFilterViewSet):
    allowed_filter_params = [{ 'field': 'enabled', 'type': ''}]
    
    def list(self, request, *args, **kwargs):
        calculate_goal_requirements(User.objects.get(pk = 2))
        return super().list(request, *args, **kwargs)

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Goal.objects.prefetch_related('requirements').all()
    serializer_class = GoalSerializer
    http_method_names = [ 'get', 'post']



# class GoalRequirementViewSet(viewsets.ModelViewSet):
#     allowed_filter_params = []

#     # authentication_classes = (TokenAuthentication,)
#     # permission_classes = (IsAuthenticated,)
#     queryset = GoalRequirement.objects.all()
#     serializer_class = GoalRequirementSerializer
#     http_method_names = [ 'get', 'post']



class ChallengeViewSet(ListFilterViewSet):
    allowed_filter_params = [{ 'field': 'enabled', 'type': ''}]
    
    def list(self, request, *args, **kwargs):
        calculate_challenge_requirements(User.objects.get(pk = 2))
        return super().list(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    # queryset = Challenge.objects.prefetch_related('requirements').all()
    
    def get_queryset(self):
        queryset = Challenge.objects.prefetch_related('requirements',
                                                      Prefetch(
                                                          'challengehistory_set',
                                                          queryset = ChallengeHistory.objects.order_by('-pk')[:1],
                                                          to_attr = 'latest_history'
                                                      )
                                                      ).all()

        return queryset
    
    serializer_class = ChallengeSerializer
    http_method_names = [ 'get', 'post', 'put']



# class ChallengeRequirementViewSet(viewsets.ModelViewSet):
#     allowed_filter_params = []

#     # authentication_classes = (TokenAuthentication,)
#     # permission_classes = (IsAuthenticated,)
#     queryset = ChallengeRequirement.objects.all()
#     serializer_class = ChallengeRequirementSerializer
#     http_method_names = [ 'get', 'post']
