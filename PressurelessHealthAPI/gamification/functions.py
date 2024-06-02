from .models import *
from health.models import *
from core.models import *
from datetime import datetime, timedelta
from django.db.models import Exists, QuerySet
from django.db.models import OuterRef, Subquery, Sum, Prefetch
from django.db.models import Count, F, Value, Q



def calculate_goal_met_requirements_count(user_id: int, goal: Goal) -> float:
    reqs_met_count = 0
    requirements = goal.requirements.all()

    total_user_measurements = Measurement.objects.filter(user_id = user_id).count()

    for req in requirements:
        if req.code == 'MEASUREMENT_AMOUNT':
            if float(req.value) <= total_user_measurements:
                reqs_met_count += 1

    return reqs_met_count



def calculate_challenge_met_requirements_count(user_id: int, challenge: Challenge, last_history: ChallengeHistory, measurements_in_date_range: QuerySet) -> float:
    reqs_met_count = 0
    requirements = challenge.requirements.all()

    time_limit = last_history.start_date + timedelta(seconds = challenge.time_limit)

    # measurements_in_date_range = Measurement.objects.filter(user_id = user_id, measurement_date__range = [last_history.start_date, time_limit]).all()
    measurements = tuple(filter(lambda m: m.measurement_date >= last_history.start_date and m.measurement_date <= time_limit, iter(measurements_in_date_range)))

    for req in requirements:
        if req.code == 'MEASUREMENT_AMOUNT':
            req_limit = last_history.start_date + (timedelta(seconds = req.time_limit) if req.time_limit else timedelta(seconds = challenge.time_limit))

            measurements_in_req_range = tuple(filter(lambda m: m.measurement_date <= req_limit, iter(measurements)))

            if len(measurements_in_req_range) >= int(req.value):
                reqs_met_count += 1

    return reqs_met_count



def calculate_challenge_met_requirements_percent(user_id: int, challenge: Challenge, last_history: ChallengeHistory) -> float:
    try:
        reqs_met_count = 0
        total_count = 0
        requirements = challenge.requirements.all()

        time_limit = last_history.start_date + timedelta(seconds = challenge.time_limit)

        measurements_in_date_range = Measurement.objects.filter(user_id = user_id, measurement_date__range = [last_history.start_date, time_limit]).all()

        for req in requirements:
            if req.code == 'MEASUREMENT_AMOUNT':
                req_limit = last_history.start_date + (timedelta(seconds = req.time_limit) if req.time_limit else timedelta(seconds = challenge.time_limit))

                measurements_in_req_range = tuple(filter(lambda m: m.measurement_date <= req_limit, iter(measurements_in_date_range)))

                count_met = len(measurements_in_req_range)

                total_count += int(req.value)
                reqs_met_count += count_met

        return reqs_met_count / total_count
    except:
        return 0



def calculate_goal_requirements(user: User):
    goals = Goal.objects.filter(enabled = True).exclude(Exists(GoalHistory.objects.filter(user = user, goal_id = OuterRef('id'))))

    created_histories = []
    new_points = 0

    for goal in goals:
        # if GoalHistory.objects.filter(user = user, goal = goal).exists():
        #     return

        reqs_met_count = calculate_goal_met_requirements_count(user, goal)

        if reqs_met_count >= goal.requirements.count():
            # last_measurement = Measurement.objects.filter(user = user).order_by('-pk').first()
            created_histories.append(
                GoalHistory(
                    user = user,
                    goal = goal,
                    reached_on = Subquery(Measurement.objects.filter(user = user).order_by('-pk').values('measurement_date')[:1])  #    last_measurement.measurement_date
                )
            )

            new_points += goal.reward

    GoalHistory.objects.bulk_create(created_histories)

    if new_points > 0:
        User.objects.filter(pk = user.pk).update(points = F('points') + new_points)



def get_measurements_in_date_range(user: User, challenges: QuerySet[Challenge]):
    measurements_in_date_range = []
    if len(challenges) > 0:
        all_histories = (next(iter(c.histories), None) for c in challenges)
        lowest_start_date_history = min(all_histories, key = lambda x: x.start_date if x else datetime.now())

        if lowest_start_date_history:
            lowest_start_date = lowest_start_date_history.start_date
        else:
            lowest_start_date = datetime.now()

        highest_limit_date = None

        for challenge in challenges:
            last_history = next(iter(challenge.histories), None)
            if last_history:
                limit_datetime = last_history.start_date + timedelta(seconds = challenge.time_limit)

                if not highest_limit_date or limit_datetime > highest_limit_date:
                    highest_limit_date = limit_datetime

        if not highest_limit_date:
            highest_limit_date = datetime.now()

        measurements_in_date_range = Measurement.objects.filter(user_id = user.pk, measurement_date__range = [ lowest_start_date, highest_limit_date ]).all()

    return measurements_in_date_range



def calculate_challenge_requirements(user: User):
    challenges = Challenge.objects.filter(
        enabled = True
    ).prefetch_related(
                  Prefetch('challengehistory_set', queryset = ChallengeHistory.objects.filter(user = user).order_by('-pk')[:1], to_attr = 'histories'), 'requirements'
              )
    # .annotate(
    #     start_time = Subquery(
    #         [:1]
    #     ),
    #     last_end_date = Subquery(
    #         ChallengeHistory.objects.filter(user = user, challenge_id = OuterRef('id'), end_date__isnull = True).values('start_date').order_by('-pk')[:1]
    #     )
    # )

    changed_histories = []
    created_histories = []
    new_points = 0

    completed_challenges = []
    failed_challenges = []

    measurements_in_date_range = get_measurements_in_date_range(user, challenges)

    for challenge in challenges:
        reqs_met_count = 0
        last_history = next(iter(challenge.histories), None)

        if last_history and not last_history.end_date:
            limit_datetime = last_history.start_date + timedelta(seconds = challenge.time_limit)

            if limit_datetime < datetime.now():
                last_history.succeeded = False
                last_history.end_date = limit_datetime
                # last_history.save()
                changed_histories.append(last_history)
                failed_challenges.append(challenge)
                # ChallengeHistory.objects.filter(user = user, challenge_id = challenge.pk, end_date__isnull = True).update(succeeded = False, end_date = limit_datetime)
            else:
                reqs_met_count = calculate_challenge_met_requirements_count(user, challenge, last_history, measurements_in_date_range)

                if reqs_met_count >= challenge.requirements.count():
                    # last_measurement = Measurement.objects.filter(user = user).order_by('-pk').first()
                    last_history.succeeded = True
                    last_history.end_date = datetime.now()
                    # last_history.save()
                    changed_histories.append(last_history)
                    new_points += challenge.reward

                    completed_challenges.append(challenge)

                    # user.save()
                    # ChallengeHistory.objects.filter(user = user, challenge_id = challenge.pk, end_date__isnull = True).update(succeeded = True, end_date = datetime.now())

        next_reset_time = (last_history.end_date if (last_history and last_history.end_date) else datetime.now()) + timedelta(days = 1)
        next_reset_time = next_reset_time.replace(hour = 0, minute = 0, second = 0, microsecond = 0)

        if challenge.repeatable and (not last_history or (datetime.now() >= next_reset_time)):
            # if not last_history or (last_history and last_history.end_date + timedelta(seconds = last_history.time_interval) < datetime.now()):
            #     new_start_date = datetime.now()
            # else:
            #     new_start_date = last_history.end_date

            new_start_date = datetime.now()

            # last_history = ChallengeHistory.objects.create(user = user, challenge = challenge, start_date = new_start_date)
            created_histories.append(ChallengeHistory(user = user, challenge = challenge, start_date = new_start_date))

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

        # limit_datetime = last_history.start_date + timedelta(seconds = challenge.time_limit)
        # if limit_datetime < datetime.now():
        #     ChallengeHistory.objects.filter(user = user, challenge_id = challenge.pk, end_date__isnull = True).update(succeeded = False, end_date = limit_datetime)
        #     continue

    ChallengeHistory.objects.bulk_update(changed_histories, [ 'succeeded', 'end_date'])
    ChallengeHistory.objects.bulk_create(created_histories)

    if new_points > 0:
        User.objects.filter(pk = user.pk).update(points = F('points') + new_points)

    return completed_challenges, failed_challenges
