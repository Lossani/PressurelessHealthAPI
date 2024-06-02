from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum, F
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import *


def recalculate_user_points(user: User):
    challengesPoints = ChallengeHistory.objects.filter(user = user, succeeded = True).aggregate(totalPoints = Sum(F('challenge__reward'))).get('totalPoints', 0)
    goalsPoints = GoalHistory.objects.filter(user = user).aggregate(totalPoints = Sum(F('goal__reward'))).get('totalPoints', 0)

    user.points = challengesPoints + goalsPoints
    user.save()



@csrf_exempt
def enviar_correo(asunto, template, datos, email):
    mensaje = render_to_string(template, datos)

    correo = EmailMultiAlternatives(asunto, strip_tags(mensaje), to = email)
    correo.attach_alternative(mensaje, "text/html")
    correo.from_email = "Apulso App <apulso@xempre.com>"
    return correo.send()
