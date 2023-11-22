from .models import *
from health.models import *
from core.models import *
from datetime import datetime, timedelta
from django.db.models import Exists
from django.db.models import OuterRef, Subquery, Sum, Prefetch
from django.db.models import Count, F, Value, Q



def calculate_goal_met_requirements_count(user_id: int, goal: Goal) -> float:
    reqs_met_count = 0
    requirements = goal.requirements.all()

    for req in requirements:
        if req.code == 'MEASUREMENT_AMOUNT':
            if float(req.value) <= Measurement.objects.filter(user_id = user_id).count():
                reqs_met_count += 1

    return reqs_met_count



def calculate_challenge_met_requirements_count(user_id: int, challenge: Challenge, last_history: ChallengeHistory) -> float:
    reqs_met_count = 0
    requirements = challenge.requirements.all()

    for req in requirements:
        if req.code == 'MEASUREMENT_AMOUNT':
            time_limit = last_history.start_date.replace(tzinfo = None) + timedelta(seconds = req.time_limit) if req.time_limit else F('measurement_date')

            if float(req.value) <= Measurement.objects.filter(user_id = user_id,
                                                              measurement_date__gte = last_history.start_date.replace(tzinfo = None),
                                                              measurement_date__lte = time_limit).count():
                reqs_met_count += 1

    return reqs_met_count



def calculate_challenge_met_requirements_percent(user_id: int, challenge: Challenge, last_history: ChallengeHistory) -> float:
    try:
        reqs_met_count = 0
        total_count = 0
        requirements = challenge.requirements.all()

        for req in requirements:
            if req.code == 'MEASUREMENT_AMOUNT':
                time_limit = last_history.start_date.replace(tzinfo = None) + timedelta(seconds = req.time_limit) if req.time_limit else F('measurement_date')

                count_met = Measurement.objects.filter(
                    user_id = user_id, measurement_date__gte = last_history.start_date.replace(tzinfo = None), measurement_date__lte = time_limit
                ).count()

                total_count += int(req.value)
                reqs_met_count += count_met

        return reqs_met_count / total_count
    except:
        return 0



def calculate_goal_requirements(user: User):
    goals = Goal.objects.filter(enabled = True).exclude(Exists(GoalHistory.objects.filter(user = user, goal_id = OuterRef('id'))))

    for goal in goals:
        # if GoalHistory.objects.filter(user = user, goal = goal).exists():
        #     return

        reqs_met_count = calculate_goal_met_requirements_count(user, goal)

        if reqs_met_count >= goal.requirements.count():
            # last_measurement = Measurement.objects.filter(user = user).order_by('-pk').first()
            GoalHistory.objects.create(
                user = user,
                goal = goal,
                reached_on = Subquery(Measurement.objects.filter(user = user).order_by('-pk').values('measurement_date')[:1])  #    last_measurement.measurement_date
            )



def calculate_challenge_requirements(user: User):
    challenges = Challenge.objects.filter(
        enabled = True
    ).exclude(Q(repeatable = False)
              & Q(Exists(ChallengeHistory.objects.filter(user = user, challenge_id = OuterRef('id'), end_date__isnull = False, succeeded = True)))).prefetch_related(
                  Prefetch(
                      'challengehistory_set', queryset = ChallengeHistory.objects.filter(user = user, end_date__isnull = True).order_by('-pk')[:1], to_attr = 'histories'
                  )
              )
    # .annotate(
    #     start_time = Subquery(
    #         [:1]
    #     ),
    #     last_end_date = Subquery(
    #         ChallengeHistory.objects.filter(user = user, challenge_id = OuterRef('id'), end_date__isnull = True).values('start_date').order_by('-pk')[:1]
    #     )
    # )

    for challenge in challenges:
        reqs_met_count = 0
        last_history = next(iter(challenge.histories), None)

        if last_history and not last_history.end_date:
            limit_datetime = last_history.start_date.replace(tzinfo = None) + timedelta(seconds = challenge.time_limit)

            if limit_datetime < datetime.now():
                last_history.succeeded = False
                last_history.end_date = limit_datetime
                last_history.save()
                # ChallengeHistory.objects.filter(user = user, challenge_id = challenge.pk, end_date__isnull = True).update(succeeded = False, end_date = limit_datetime)
            else:
                reqs_met_count = calculate_challenge_met_requirements_count(user, challenge, last_history)

                if reqs_met_count >= challenge.requirements.count():
                    # last_measurement = Measurement.objects.filter(user = user).order_by('-pk').first()
                    last_history.succeeded = True
                    last_history.end_date = datetime.now()
                    last_history.save()
                    # ChallengeHistory.objects.filter(user = user, challenge_id = challenge.pk, end_date__isnull = True).update(succeeded = True, end_date = datetime.now())

        if challenge.repeatable and (not last_history or (last_history and last_history.end_date)):
            # if not last_history or (last_history and last_history.end_date + timedelta(seconds = last_history.time_interval) < datetime.now()):
            #     new_start_date = datetime.now()
            # else:
            #     new_start_date = last_history.end_date

            new_start_date = datetime.now()

            last_history = ChallengeHistory.objects.create(user = user, challenge = challenge, start_date = new_start_date)

        # if challenge.repeatable and (not last_history or last_history.end_date):
        #     # if last_history and last_history.end_date + timedelta(seconds = last_history.time_interval):
        #     #     continue

        #     if not last_history or last_history.end_date + timedelta(seconds = last_history.time_interval) < datetime.now():
        #         new_start_date = datetime.now()
        #     else:
        #         new_start_date = last_history.end_date

        #     last_history = ChallengeHistory.objects.create(
        #         user = user,
        #         challenge = challenge,
        #         start_date = new_start_date
        #     )

        # if not challenge.repeatable or not last_history:
        #     continue

        # limit_datetime = last_history.start_date.replace(tzinfo = None) + timedelta(seconds = challenge.time_limit)
        # if limit_datetime < datetime.now():
        #     ChallengeHistory.objects.filter(user = user, challenge_id = challenge.pk, end_date__isnull = True).update(succeeded = False, end_date = limit_datetime)
        #     continue
