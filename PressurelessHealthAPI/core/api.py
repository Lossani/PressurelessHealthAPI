from .serializers import *
from .models import *
from rest_framework import viewsets



class UserViewSet(viewsets.ModelViewSet):
    allowed_filter_params = [{ 'field': 'email', 'type': ''}]

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



class MedicationViewSet(viewsets.ModelViewSet):
    allowed_filter_params = []

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']



class MedicationFrequencyViewSet(viewsets.ModelViewSet):
    allowed_filter_params = []

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = MedicationFrequency.objects.all()
    serializer_class = MedicationFrequencySerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']



class ReminderViewSet(viewsets.ModelViewSet):
    allowed_filter_params = []

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']



class GoalHistoryViewSet(viewsets.ModelViewSet):
    allowed_filter_params = []

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = GoalHistory.objects.all()
    serializer_class = GoalHistorySerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']



class ChallengeHistoryViewSet(viewsets.ModelViewSet):
    allowed_filter_params = []

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = ChallengeHistory.objects.all()
    serializer_class = ChallengeHistorySerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']



class NotificationHistoryViewSet(viewsets.ModelViewSet):
    allowed_filter_params = []

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = NotificationHistory.objects.all()
    serializer_class = NotificationHistorySerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']
