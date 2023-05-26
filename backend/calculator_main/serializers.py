from rest_framework import serializers

from .models import Offer


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('city_name', 'category_offer', 'name_offer', 'price', 'discount')
        depth = 1

