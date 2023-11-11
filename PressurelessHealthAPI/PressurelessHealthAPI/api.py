import json
from django.http import HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError, JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets
from django.utils.translation import gettext as _

class ListFilterViewSet(viewsets.ModelViewSet):
    allowed_filter_params = []
    
    def _check_if_filter_present(self, get_request):
        found_params = {}
        for param in self.allowed_filter_params:
            param_value = get_request.get(param.get('name', param['field']), '')
            if param_value != '':
                lookup_param = (param.get('related_object', '')) + param['field'] + (param.get('type', ''))
                found_params[lookup_param] = param_value

        return found_params
    
    def list(self, request, *args, **kwargs):
        # if not request.user.is_authenticated:
        #     return Response(_("No ha iniciado sesión."), status = 401)
        
        filter_params = self._check_if_filter_present(request.GET)
        
        lista = self.get_queryset()

        if len(filter_params) == 0:
            usuarios = self.serializer_class(lista, many = True)
            return Response(data = usuarios.data)

        lista = lista.filter(**filter_params)

        serializer = self.serializer_class(lista, many = True)

        responseFormat = request.GET.get('format')

        if responseFormat == 'json':
            return JsonResponse(serializer.data, safe = False)

        return Response(data = serializer.data)