from .serializers import *
from .models import *
from rest_framework import viewsets
from PressurelessHealthAPI.api import *
from .functions import *



class UserViewSet(viewsets.ModelViewSet):
    allowed_filter_params = [{ 'field': 'email', 'type': ''}]
    
    # def retrieve(self, request, pk = None, *args, **kwargs):
    #     recalculate_user_points(User.objects.get(pk = int(pk)))
    #     return super().retrieve(request, pk, *args, **kwargs)

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']



class ContactViewSet(viewsets.ModelViewSet):
    allowed_filter_params = []

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']




class ReminderViewSet(viewsets.ModelViewSet):
    allowed_filter_params = []

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']



class GoalHistoryViewSet(ListFilterViewSet):
    allowed_filter_params = [{ 'field': 'goal', 'type': ''}]

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = GoalHistory.objects.prefetch_related('goal', 'goal__requirements').all()
    serializer_class = GoalHistorySerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']



class ChallengeHistoryViewSet(ListFilterViewSet):
    allowed_filter_params = [{ 'field': 'succeeded', 'type': ''}, { 'field': 'challenge', 'type': ''}]

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = ChallengeHistory.objects.prefetch_related('challenge', 'challenge__requirements').all()
    serializer_class = ChallengeHistorySerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']



class NotificationHistoryViewSet(viewsets.ModelViewSet):
    allowed_filter_params = []

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = NotificationHistory.objects.all()
    serializer_class = NotificationHistorySerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']
