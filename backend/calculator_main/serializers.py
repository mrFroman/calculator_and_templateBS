from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import Offer, CategoryOffer, City, ListAllUrls, CitiesTemplate, User

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

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize CustomUser model.
    """

    class Meta:
        model = User
        fields = ("id", "email")


class UserRegisterationSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize registration requests and create a new user.
    """

    class Meta:
        model = User
        fields = ("id", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer class to authenticate users with email and password.
    """

    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class ListAllUrlsSerializer(serializers.ModelSerializer):
    user_create = serializers.StringRelatedField()
    type_mail = serializers.StringRelatedField()

    class Meta:
        model = ListAllUrls
        fields = ('id', 'date_create_mail', 'type_mail', 'user_create', 'urls_content', 'urls_transfer')
        depth = 1


class CitiesTemplateSerializer(serializers.ModelSerializer):
    list_city = ListAllUrlsSerializer(many=True)

    class Meta:
        model = CitiesTemplate
        fields = ('id', 'city', 'list_city')
