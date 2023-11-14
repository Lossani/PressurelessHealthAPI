from rest_framework import routers
from .views import *
from django.urls import path
from .api import *

router = routers.DefaultRouter()


# router.register('departamento', DepartamentoViewSet, 'departamento')
# router.register('provincia', ProvinciaViewSet, 'provincia')
# router.register('distrito', DistritoViewSet, 'distrito')
router.register('requirements', RequirementViewSet, 'requirements')
router.register('goals', GoalViewSet, 'goals')
# router.register('goal_requirements', GoalRequirementViewSet, 'goal_requirements')
router.register('challenges', ChallengeViewSet, 'challenges')
# router.register('challenge_requirements', ChallengeViewSet, 'challenge_requirements')


urlpatterns = [
    # path('getDepartamento/<idPais>', getDepartamento, name= 'getDepartamento'),
    # path('getProvincia/<idDepartamento>', getProvincia, name= 'getProvincia'),
    # path('getDistrito/<idProvincia>', getDistrito, name= 'getDistrito'),
] + router.urls