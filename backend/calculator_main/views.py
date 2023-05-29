
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Offer, City
from .serializers import OfferSerializer, CitySerializer


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


