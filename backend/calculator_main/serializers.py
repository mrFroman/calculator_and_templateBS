from rest_framework import serializers

from .models import Offer, CategoryOffer, City


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryOffer
        field = ('name_offer', 'price', 'discount')


class CategorySerializer(serializers.ModelSerializer):
    #offer = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = CategoryOffer
        fields = ('title', 'offer')
        #exclude = ('id', 'category_offer')
        depth = 1


class CitySerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ('city_name', 'categories')





