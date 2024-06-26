# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from random import randint

from django.shortcuts import render
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from core.models import User
from core.functions import enviar_correo
from rest_framework import viewsets

# Create your views here.



class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format = None):
        serializer = AuthTokenSerializer(data = request.data)
        serializer.is_valid(raise_exception = False)

        if serializer.errors != {}:
            return Response("Usuario no registrado/habilitado o datos incorrectos: " + ", ".join(serializer.error_messages), status = 401)

        user = serializer.validated_data['user']

        login(request, user)
        return super(LoginView, self).post(request, format = None)



class RetrievePasswordResetCode(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny, )
    http_method_names = ['post']

    def create(self, request):
        if request.method == 'POST':
            user = User.objects.filter(email = request.data.get('email', None)).first()

            if user:
                if user.password_reset_code_last_request:
                    last_request = datetime.now() - user.password_reset_code_last_request
                    
                    if last_request.seconds < 60:
                        return Response({ "response": "Ha solicitado el código hace %s segundos, debe esperar un minuto para solicitar otro." % (last_request.seconds)}, status = 403)
                
                asunto = "Apulso - Cambia tu Contraseña"
                template = "template_change_password.html"
                code = randint(1000000, 9999999)
                user.password_reset_code = code
                user.password_reset_code_last_request = datetime.now()
                user.save()
                datos = {
                    'user': user,
                    'code': code,
                }
                if enviar_correo(asunto, template, datos, [user.email]):
                    return Response({ "response": "Correo enviado."}, status = 200)
                else:
                    return Response({ "response": "Correo no enviado."}, status = 500)
            else:
                return Response({ "response": "No existe usuario asociado."}, status = 404)
        else:
            return Response({ "response": "Solicitud incorrecta."}, status = 400)



class UserUpdatePassword(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny, )
    http_method_names = ['put', 'patch']

    def update(self, request, *args, **kwargs):
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        password_change_code = request.data.get('password_change_code', '')
        user = User.objects.filter(email = email).first()
        
        if not user:
            return Response({ "response": "No existe usuario asociado."}, status = 404)
        
        if password and password_change_code:
            if user.password_reset_code == str(password_change_code):
                user.set_password(password)
                user.password_reset_code = None
                user.save()
                return Response({ "response": "Contraseña cambiada correctamente."}, status = 200)
            else:
                return Response({ "response": "El código de cambio de contraseña no es válido."}, status = 403)
        
        return Response({ "response": "Por favor, ingrese el email del usuario, la contraseña nueva y el código de verificación."}, status = 400)
    
    
    
def test(request):
    asunto = "Apulso - Prueba"
    template = "template_test.html"
    
    enviar_correo(asunto, template, {}, ['dev@xempre.com'])