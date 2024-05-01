from random import randint

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from health.models import Article, Measurement
from health.serializers import ArticleSerializer, MeasurementSerializer
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication

# Create your views here.



class RetrieveRandomArticle(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        articles_pks = Article.objects.values_list('pk', flat = True)
        articles_quantity = len(articles_pks)

        if articles_quantity == 0:
            return []
        random_index = randint(0, articles_quantity - 1)
        article = Article.objects.get(pk = articles_pks[random_index])
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status = 200)



class RetrieveLatestMeasurement(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        measurement = Measurement.objects.filter(user = request.user.pk).order_by('-pk').first()

        serializer = MeasurementSerializer(measurement)
        return Response(serializer.data, status = 200)
