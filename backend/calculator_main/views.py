
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import City, ListAllUrls, CitiesTemplate
from .serializers import CitySerializer, ListAllUrlsSerializer, CitiesTemplateSerializer


class OfferApiView(viewsets.ModelViewSet):
    ''' апи для всех  обьектов модели цены калькулятора '''
    queryset = City.objects.all()
    serializer_class = CitySerializer


class OfferPostApiView(APIView):
    def get(self, request):
        return Response({'aaa': 'bbbb'})

    def post(self, request):
        date = request.POST
        return Response(date)


''' Api для моделей шаблонизатора '''

class ListAllUrlsApiView(viewsets.ModelViewSet):
    queryset = ListAllUrls.objects.all()
    serializer_class = ListAllUrlsSerializer


class CitiesTemplateApiView(viewsets.ModelViewSet):
    queryset = CitiesTemplate.objects.all()
    serializer_class = CitiesTemplateSerializer