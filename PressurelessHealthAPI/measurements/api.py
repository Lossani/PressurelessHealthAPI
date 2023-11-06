from .serializers import *
from .models import *
from rest_framework import viewsets

class MeasurementViewSet(viewsets.ModelViewSet):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    http_method_names = ['get', 'post']