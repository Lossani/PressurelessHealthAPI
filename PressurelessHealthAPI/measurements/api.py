from .serializers import *
from .models import *
from rest_framework import viewsets
from PressurelessHealthAPI.api import *

class MeasurementViewSet(ListFilterViewSet):
    allowed_filter_params = [
        {
            'name': 'measurement_date_start',
            'field': 'measurementDate',
            'type': '__gte',
        },
        {
            'name': 'measurement_date_end',
            'field': 'measurementDate',
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
        queryset = Measurement.objects.all()

        return queryset
    
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    # queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    http_method_names = ['get', 'post']