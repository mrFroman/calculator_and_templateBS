from django.urls import path, include
from rest_framework import routers, request
from .views import OfferApiView, ListAllUrlsApiView, CitiesTemplateApiView, UserLoginAPIView, UserRegisterationAPIView, \
    UserLogoutAPIView

router = routers.DefaultRouter()
router.register(r'calculator', OfferApiView, basename='calculator')
router.register(r'postdate', ListAllUrlsApiView, basename='postdate')
router.register(r'cities', CitiesTemplateApiView, basename='cities')


urlpatterns = [
    path('', include(router.urls)),
    path("register/", UserRegisterationAPIView.as_view(), name="create-user"),
    path("login/", UserLoginAPIView.as_view(), name="login-user"),
    path("logout/", UserLogoutAPIView.as_view(), name="logout-user"),
]

