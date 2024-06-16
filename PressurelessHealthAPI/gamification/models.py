from django.db import models

# Create your models here.




class Requirement(models.Model):
    code = models.CharField(null = False, max_length = 50)
    value = models.CharField(null = False, max_length = 50)
    required = models.BooleanField(null = False, default = True)
    time_limit = models.CharField(null = True, max_length = 50)
    distinct_days = models.BooleanField(null = False, default = False)
    # goal_required = models.ForeignKey(Goal, on_delete = models.CASCADE, null = True)
    
    
class Goal(models.Model):
    name = models.CharField(null = False, max_length = 50)
    description = models.CharField(null = False, max_length = 255)
    image = models.CharField(null = False, max_length = 255)
    reward = models.PositiveIntegerField(null = False)
    enabled = models.BooleanField(null = False, default = True)
    requirements = models.ManyToManyField(Requirement)


# class GoalRequirement(models.Model):
#     goal = models.ForeignKey(Goal, on_delete = models.CASCADE, null = False)
#     requirement = models.ForeignKey(Requirement, on_delete = models.CASCADE, null = False)



class Challenge(models.Model):
    name = models.CharField(null = False, max_length = 50)
    description = models.CharField(null = False, max_length = 255)
    image = models.CharField(null = False, max_length = 255)
    reward = models.PositiveIntegerField(null = False)
    time_limit = models.BigIntegerField(null = True)
    enabled = models.BooleanField(null = False, default = True)
    repeatable = models.BooleanField(null = False, default = False)
    repetition_interval = models.PositiveIntegerField(null = True)
    requirements = models.ManyToManyField(Requirement)
    order = models.IntegerField(null = False, default = 0)