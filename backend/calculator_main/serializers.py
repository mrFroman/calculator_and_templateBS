from rest_framework import serializers

from .models import Offer, CategoryOffer, City

''' сериализатор для калькулятора '''


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('name_offer', 'price', 'discount')


class CategorySerializer(serializers.ModelSerializer):
    offer = OfferSerializer(many=True, read_only=True)

    class Meta:
        model = CategoryOffer
        fields = ('title', 'offer')


class CitySerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ('id', 'city_name', 'categories')





