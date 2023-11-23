from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from .models import *
from health.models import *
from datetime import datetime
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def generate_leaderboard(request):
    if request.method == 'GET':
        users = User.objects.order_by('-points').all()
        
        result = [{
            'first_name': u.first_name,
            'last_name': u.last_name,
            'username': u.username,
            'points': u.points
        } for u in users]
        
        return JsonResponse(result, safe = False)
    else:
        return HttpResponseBadRequest('Method not allowed.')