from rest_framework import routers
from .views import *
from django.urls import path
from .api import *

router = routers.DefaultRouter()


# router.register('departamento', DepartamentoViewSet, 'departamento')
# router.register('provincia', ProvinciaViewSet, 'provincia')
# router.register('distrito', DistritoViewSet, 'distrito')
router.register('all', MeasurementViewSet, 'measurements')

urlpatterns = [
    # path('getDepartamento/<idPais>', getDepartamento, name= 'getDepartamento'),
    # path('getProvincia/<idDepartamento>', getProvincia, name= 'getProvincia'),
    # path('getDistrito/<idProvincia>', getDistrito, name= 'getDistrito'),
] + router.urls