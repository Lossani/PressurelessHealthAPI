from rest_framework import routers
from .views import *
from django.urls import path
from .api import *

router = routers.DefaultRouter()


# router.register('departamento', DepartamentoViewSet, 'departamento')
# router.register('provincia', ProvinciaViewSet, 'provincia')
# router.register('distrito', DistritoViewSet, 'distrito')
router.register(r'users/?', UserViewSet, 'users')
router.register(r'contacts/?', ContactViewSet, 'contacts')
router.register(r'reminders/?', ReminderViewSet, 'reminders')
router.register(r'goal_history/?', GoalHistoryViewSet, 'goal_history')
router.register(r'challenge_history/?', ChallengeHistoryViewSet, 'challenges_history')
router.register(r'notification_history/?', NotificationHistoryViewSet, 'notifications_history')


urlpatterns = [
    # path('getDepartamento/<idPais>', getDepartamento, name= 'getDepartamento'),
    # path('getProvincia/<idDepartamento>', getProvincia, name= 'getProvincia'),
    # path('getDistrito/<idProvincia>', getDistrito, name= 'getDistrito'),
] + router.urls