from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication

from .serializers import *
from .models import *
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

    def get_queryset(self):
        queryset = Medication.objects.filter(deleted = False, user = self.request.user.pk)
        return queryset



class MedicationFrequencyViewSet(ListFilterViewSet):
    allowed_filter_params = [
        {
            'field': 'medication',
        },
    ]

    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    queryset = MedicationFrequency.objects.all()
    serializer_class = MedicationFrequencySerializer
    http_method_names = [ 'get', 'post', 'put', 'patch']

    def get_queryset(self):
        queryset = MedicationFrequency.objects.filter(medication__user = self.request.user.pk)
        return queryset
