from .models import *
from health.models import *
from datetime import datetime, timedelta
from django.db.models import Exists
from django.db.models import OuterRef, Subquery, Sum
from django.db.models import Count, F, Value



def calculate_goal_requirements(user: User):
    goals = Goal.objects.filter(enabled = True).exclude(Exists(GoalHistory.objects.filter(user = user, goal_id = OuterRef('id'))))

    for goal in goals:
        # if GoalHistory.objects.filter(user = user, goal = goal).exists():
        #     return

        reqs_met_count = 0
        requirements = goal.requirements.all()

        if len(requirements) == 0:
            continue

        for req in requirements:
            if req.code == 'MEASUREMENT_AMOUNT':
                if float(req.value) <= Measurement.objects.filter(user = user).count():
                    reqs_met_count += 1

        if reqs_met_count == len(requirements):
            # last_measurement = Measurement.objects.filter(user = user).order_by('-pk').first()
            GoalHistory.objects.create(
                user = user,
                goal = goal,
                reached_on = Subquery(Measurement.objects.filter(user = user).order_by('-pk').values('measurement_date')[:1])  #    last_measurement.measurement_date
            )



def calculate_challenge_requirements(user: User):
    challenges = Challenge.objects.filter(enabled = True).exclude(
        Exists(ChallengeHistory.objects.filter(user = user, challenge_id = OuterRef('id'), end_date__isnull = False, succeeded = True))
    ).annotate(
        start_time = Subquery(
            ChallengeHistory.objects.filter(user = user, challenge_id = OuterRef('id'), end_date__isnull = True).values('start_date').order_by('-pk')[:1]
        )
    )

    for challenge in challenges:
        reqs_met_count = 0

        if challenge.start_time.replace(tzinfo = None) + timedelta(seconds = challenge.time_limit) < datetime.now():
            ChallengeHistory.objects.filter(user = user, challenge_id = challenge.pk, end_date__isnull = True).update(succeeded = False, end_date = datetime.now())
            continue

        requirements = challenge.requirements.all()

        if len(requirements) == 0:
            continue

        for req in requirements:
            if req.code == 'MEASUREMENT_AMOUNT':
                time_limit = challenge.start_time.replace(tzinfo = None) + timedelta(seconds = req.time_limit) if req.time_limit else F('measurement_date')

                if float(req.value) <= Measurement.objects.filter(user = user,
                                                                  measurement_date__gte = challenge.start_time.replace(tzinfo = None),
                                                                  measurement_date__lte = time_limit).count():
                    reqs_met_count += 1

        if reqs_met_count == len(requirements):
            # last_measurement = Measurement.objects.filter(user = user).order_by('-pk').first()
            ChallengeHistory.objects.filter(user = user, challenge_id = challenge.pk, end_date__isnull = True).update(succeeded = True, end_date = datetime.now())
