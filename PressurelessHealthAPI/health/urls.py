from rest_framework import routers
from .views import *
from django.urls import path
from .api import *

router = routers.DefaultRouter()


# router.register('departamento', DepartamentoViewSet, 'departamento')
# router.register('provincia', ProvinciaViewSet, 'provincia')
# router.register('distrito', DistritoViewSet, 'distrito')
router.register(r'measurements/?', MeasurementViewSet, 'measurements')
router.register(r'medications/?', MedicationViewSet, 'medications')
router.register(r'medication_frequencies/?', MedicationFrequencyViewSet, 'medication_frequencies')
# router.register(r'articles/?', ArticlesViewSet, 'articles')

urlpatterns = [
    path(r'measurements/latest/', RetrieveLatestMeasurement.as_view({'get': 'get'}), name = 'measurements_latest'),
    path(r'articles/random/', RetrieveRandomArticle.as_view({'get': 'get'}), name = 'article_random')
] + router.urls