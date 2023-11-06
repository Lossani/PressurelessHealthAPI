from .serializers import *
from .models import *
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    allowed_filter_params = [{ 'field': 'email', 'type': ''}]
    
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get','post']