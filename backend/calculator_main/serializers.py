from rest_framework import serializers

from .models import Offer, CategoryOffer, City, ListAllUrls, CitiesTemplate

''' сериализатор для калькулятора '''


class OfferSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = Offer
        fields = ('name_offer', 'price', 'discount')

    def get_price(self, obj):
        return round(obj.price / 7, 1)


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


''' сериализаторы для шаблонизатора '''


class ListAllUrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListAllUrls
        fields = '__all__'
        depth = 1


class CitiesTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitiesTemplate
        fields = '__all__'
