
from rest_framework import viewsets

from .models import Offer
from .serializers import OfferSerializer


class OfferApiView(viewsets.ModelViewSet):
    ''' апи для всех  обьектов модели цены калькулятора '''
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

