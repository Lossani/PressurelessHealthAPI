from rest_framework import routers
from django.urls import path
from knox import views as knox_views

from .views import *
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
router.register(r'debug_logs/?', DebugLogViewSet, 'debug_logs')

urlpatterns = [
    # KNOX Token
    path(r'login/', LoginView.as_view(), name = 'knox_login'),
    path(r'logout/', knox_views.LogoutView.as_view(), name = 'knox_logout'),
    path(r'logoutall/', knox_views.LogoutAllView.as_view(), name = 'knox_logoutall'),
    path(r'password_reset/', RetrievePasswordResetCode.as_view({'post': 'create'}), name = 'password_reset'),
    path(r'password_change/', UserUpdatePassword.as_view({'put': 'update'}), name='password_change' ),
    # path(r'test/', test, name="test")
    
] + router.urls
