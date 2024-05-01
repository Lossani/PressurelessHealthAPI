from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication

from .serializers import *
from .models import *

from PressurelessHealthAPI.api import *
from .functions import *

from .auth import AllowPOSTWithoutToken, AllowPUTWithoutToken, AllowPOSTPUTWithoutToken



class UserViewSet(viewsets.ModelViewSet):
    allowed_filter_params = [{ 'field': 'email', 'type': ''}]

    # def retrieve(self, request, pk = None, *args, **kwargs):
    #     recalculate_user_points(User.objects.get(pk = int(pk)))
    #     return super().retrieve(request, pk, *args, **kwargs)

    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowPOSTWithoutToken, )
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']

    # authentication_classes = (TokenAuthentication, )

    def create(self, request, *args, **kwargs):
        if User.objects.filter(username = request.data.get('username')).exists():
            return Response({ "response": "Username already exists."}, status = 400)

        if User.objects.filter(email = request.data.get('email')).exists():
            return Response({ "response": "Email already exists."}, status = 400)

        new_user = User.objects.create_user(**request.data, is_active = True)
        return Response(UserSerializer(new_user).data)

    def partial_update(self, request, pk = None, *args, **kwargs):
        password = request.data.get('password', '')
        password_change_code = request.data.get('password_change_code', '')
        user = User.objects.get(pk = pk)

        if password and password_change_code:
            if user.password_reset_code == str(password_change_code):
                user.set_password(password)
                user.save()
            else:
                return Response({ "response": "Password change code is not valid."}, status = 403)

        return super().partial_update(request, *args, **kwargs)

    def get_queryset(self):
        queryset = User.objects.filter(pk = self.request.user.pk)
        return queryset



class ContactViewSet(viewsets.ModelViewSet):
    allowed_filter_params = []

    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    # queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']

    def create(self, request, *args, **kwargs):
        serializer = ContactSerializer(data = request.data, context = { 'request': request })
        if not serializer.is_valid():
            return Response(serializer.errors, status = 400)
        serializer.save(user_id = request.user.pk)
        return Response(serializer.data, status = 201)

    def get_queryset(self):
        queryset = Contact.objects.filter(user = self.request.user.pk, deleted = False)
        return queryset



class ReminderViewSet(viewsets.ModelViewSet):
    allowed_filter_params = []

    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    # queryset = Reminder.objects.all()
    serializer_class = DetailedReminderSerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']

    def get_queryset(self):
        queryset = Reminder.objects.select_related('medication_frequency', 'medication_frequency__medication').filter(medication_frequency__medication__user = self.request.user.pk)
        return queryset



class GoalHistoryViewSet(ListFilterViewSet):
    allowed_filter_params = [{ 'field': 'goal', 'type': ''}]

    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    # queryset = GoalHistory.objects.prefetch_related('goal', 'goal__requirements').all()
    serializer_class = GoalHistorySerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']

    def get_queryset(self):
        queryset = GoalHistory.objects.prefetch_related('goal', 'goal__requirements').filter(user = self.request.user.pk)
        return queryset



class ChallengeHistoryViewSet(ListFilterViewSet):
    allowed_filter_params = [{ 'field': 'succeeded', 'type': ''}, { 'field': 'challenge', 'type': ''}]

    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    # queryset = ChallengeHistory.objects.prefetch_related('challenge', 'challenge__requirements').all()
    serializer_class = ChallengeHistorySerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']

    def create(self, request, *args, **kwargs):
        serializer = ChallengeHistorySerializer(data = request.data, context = { 'request': request })
        if not serializer.is_valid():
            return Response(serializer.errors, status = 400)
        serializer.save(user_id = request.user.pk, start_date = datetime.now())
        return Response(serializer.data, status = 201)

    def get_queryset(self):
        queryset = ChallengeHistory.objects.prefetch_related('challenge', 'challenge__requirements').filter(user = self.request.user.pk)
        return queryset



class NotificationHistoryViewSet(viewsets.ModelViewSet):
    allowed_filter_params = []

    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    # queryset = NotificationHistory.objects.all()
    serializer_class = NotificationHistorySerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']

    def get_queryset(self):
        queryset = NotificationHistory.objects.filter(user = self.request.user.pk)
        return queryset
