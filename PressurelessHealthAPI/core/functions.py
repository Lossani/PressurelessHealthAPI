from .models import *
from django.db.models import Sum, F

def recalculate_user_points(user: User):
    challengesPoints = ChallengeHistory.objects.filter(user = user, succeeded = True).aggregate(totalPoints = Sum(F('challenge__reward'))).get('totalPoints', 0)
    goalsPoints = GoalHistory.objects.filter(user = user).aggregate(totalPoints = Sum(F('goal__reward'))).get('totalPoints', 0)
    
    user.points = challengesPoints + goalsPoints
    user.save()