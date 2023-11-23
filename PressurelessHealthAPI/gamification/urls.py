from rest_framework import routers
from .views import *
from django.urls import path, re_path
from .api import *



router = routers.DefaultRouter()

# router.register('departamento', DepartamentoViewSet, 'departamento')
# router.register('provincia', ProvinciaViewSet, 'provincia')
# router.register('distrito', DistritoViewSet, 'distrito')
router.register(r'requirements/?', RequirementViewSet, 'requirements')
router.register(r'goals/?', GoalViewSet, 'goals')
# router.register('goal_requirements', GoalRequirementViewSet, 'goal_requirements')
router.register(r'challenges/?', ChallengeViewSet, 'challenges')
# router.register(r'leaderboard/?', generate_leaderboard, 'leaderboard')
# router.register('challenge_requirements', ChallengeViewSet, 'challenge_requirements')

urlpatterns = [
    re_path(r'leaderboard/?', generate_leaderboard, name = 'leaderboard'),
    # re_path(r"^requirements\/?$", RequirementViewSet, name='requirements'),
    # re_path(r"^goals\/?$", GoalViewSet, name='goals'),
    # re_path(r"^challenges\/?$", ChallengeViewSet, name='challenges'),
    # path('getDepartamento/<idPais>', getDepartamento, name= 'getDepartamento'),
    # path('getProvincia/<idDepartamento>', getProvincia, name= 'getProvincia'),
    # path('getDistrito/<idProvincia>', getDistrito, name= 'getDistrito'),
] + router.urls
