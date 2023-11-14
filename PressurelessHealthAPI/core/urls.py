from rest_framework import routers
from .views import *
from django.urls import path
from .api import *

router = routers.DefaultRouter()


# router.register('departamento', DepartamentoViewSet, 'departamento')
# router.register('provincia', ProvinciaViewSet, 'provincia')
# router.register('distrito', DistritoViewSet, 'distrito')
router.register('users', UserViewSet, 'users')
router.register('contacts', ContactViewSet, 'contacts')
router.register('medications', MedicationViewSet, 'medications')
router.register('medication_frequencies', MedicationFrequencyViewSet, 'medication_frequencies')
router.register('reminders', ReminderViewSet, 'reminders')
router.register('goal_history', GoalHistoryViewSet, 'goal_history')
router.register('challenge_history', ChallengeHistoryViewSet, 'challenges_history')
router.register('notification_history', NotificationHistoryViewSet, 'notifications_history')


urlpatterns = [
    # path('getDepartamento/<idPais>', getDepartamento, name= 'getDepartamento'),
    # path('getProvincia/<idDepartamento>', getProvincia, name= 'getProvincia'),
    # path('getDistrito/<idProvincia>', getDistrito, name= 'getDistrito'),
] + router.urls