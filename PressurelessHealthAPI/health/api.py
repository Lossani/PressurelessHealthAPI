from random import randint

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from django.db.models.aggregates import Count
from django.db.models import QuerySet, Prefetch

from .serializers import *
from .models import *
from core.models import Reminder
from PressurelessHealthAPI.api import *



class MeasurementViewSet(ListFilterViewSet):
    allowed_filter_params = [
        {
            'name': 'measurement_date_start',
            'field': 'measurement_date',
            'type': '__gte',
        },
        {
            'name': 'measurement_date_end',
            'field': 'measurement_date',
            'type': '__lte',
        },
    ]

    def list(self, request):
        # currentUser = request.user
        filter_params = self._check_if_filter_present(request.GET)

        lista = self.get_queryset()

        if len(filter_params) == 0:
            measurements = self.serializer_class(lista, many = True, context = { 'request': request })
            return Response(data = measurements.data)

        lista = lista.filter(**filter_params)

        serializer = self.serializer_class(lista, many = True, context = { 'request': request })

        responseFormat = request.GET.get('format')

        if responseFormat == 'json':
            return JsonResponse(serializer.data, safe = False)

        return Response(data = serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = MeasurementSerializer(data = request.data, context = { 'request': request })
        if not serializer.is_valid():
            return Response(serializer.errors, status = 400)
        serializer.save(user_id = request.user.pk)
        return Response(serializer.data, status = 201)

    def get_queryset(self):
        queryset = Measurement.objects.filter(user = self.request.user.pk)

        return queryset

    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    # queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    http_method_names = [ 'get', 'post']



class MedicationViewSet(viewsets.ModelViewSet):
    allowed_filter_params = []

    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    # queryset = Medication.objects.filter(deleted = False)
    serializer_class = MedicationSerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']

    def create(self, request, *args, **kwargs):
        serializer = MedicationSerializer(data = request.data, context = { 'request': request })
        if not serializer.is_valid():
            return Response(serializer.errors, status = 400)
        serializer.save(user_id = request.user.pk)
        return Response(serializer.data, status = 201)

    def get_queryset(self):
        queryset = Medication.objects.filter(
            deleted = False, user = self.request.user.pk
        ).prefetch_related(Prefetch('medicationfrequency_set', queryset = MedicationFrequency.objects.filter(deleted = False), to_attr = 'medication_frequencies'))
        return queryset



class MedicationFrequencyViewSet(ListFilterViewSet):
    allowed_filter_params = [
        {
            'field': 'medication',
        },
    ]

    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    # queryset = MedicationFrequency.objects.all()
    serializer_class = MedicationFrequencySerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']

    def create(self, request, *args, **kwargs):
        serializer = MedicationFrequencySerializer(data = request.data, context = { 'request': request })
        if not any((
                request.data.get('monday', False),
                request.data.get('tuesday', False),
                request.data.get('wednesday', False),
                request.data.get('thursday', False),
                request.data.get('friday', False),
                request.data.get('saturday', False),
                request.data.get('sunday', False),
        )):
            return Response({ "response": "Debe seleccionar al menos un día de la semana."}, status = 400)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status = 400)

        serializer.save()

        return Response(serializer.data, status = 201)

    def get_queryset(self):
        queryset = MedicationFrequency.objects.select_related('reminder', 'medication').filter(medication__user = self.request.user.pk, deleted = False)
        return queryset



class ArticlesViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = ArticleSerializer
    http_method_names = ['get']

    def get_queryset(self):
        return Article.objects.filter(enabled = True)
