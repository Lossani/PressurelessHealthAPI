from django.shortcuts import render
from .models import *
from health.models import *
from datetime import datetime

# Create your views here.



def calculate_requirements(user: User):
    goals = Goal.objects.filter(enabled = True)
    for goal in goals:
        if GoalHistory.objects.filter(user = user, goal = goal).exists():
            return
        
        reqs_met_count = 0
        requirements = goal.requirements.all()
        
        if len(requirements) == 0:
            continue
        
        for req in requirements:
            if req.code == 'MEASUREMENT_AMOUNT':
                if int(req.value) <= Measurement.objects.filter(user = user).count():
                    reqs_met_count += 1

        if reqs_met_count == goal.requirements.count():
            last_measurement = Measurement.objects.filter(user = user).order_by('-pk').first()
            GoalHistory.objects.create(user = user, goal = goal, reached_on = last_measurement.measurement_date)
