from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import City, ListAllUrls, CitiesTemplate, User
from .serializers import CitySerializer, ListAllUrlsSerializer, CitiesTemplateSerializer, UserRegisterationSerializer, \
    UserLoginSerializer, UserSerializer


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


class UserRegisterationAPIView(GenericAPIView):
    """
    An endpoint for the client to create a new User.
    """

    User = get_user_model()

    permission_classes = (AllowAny,)
    serializer_class = UserRegisterationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(GenericAPIView):
    """
    An endpoint to authenticate existing users using their email and password.
    """
    User = get_user_model()

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = UserSerializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_200_OK)


class UserLogoutAPIView(GenericAPIView):
    """
    An endpoint to logout users.
    """
    User = get_user_model()
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(RetrieveUpdateAPIView):
    """
    Get, Update user information
    """
    User = get_user_model()

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ListAllUrlsApiView(viewsets.ModelViewSet):
    queryset = ListAllUrls.objects.all()
    serializer_class = ListAllUrlsSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )


class CitiesTemplateApiView(viewsets.ModelViewSet):
    queryset = CitiesTemplate.objects.all()
    serializer_class = CitiesTemplateSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication, )

