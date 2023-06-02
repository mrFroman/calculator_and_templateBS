from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, request
from .views import OfferApiView, ListAllUrlsApiView, CitiesTemplateApiView, UserLoginAPIView, UserRegisterationAPIView, \
    UserLogoutAPIView, OfferPostApiView

router = routers.DefaultRouter()
router.register(r'calculator', OfferApiView, basename='calculator')
router.register(r'postdate', ListAllUrlsApiView, basename='postdate')
router.register(r'cities', CitiesTemplateApiView, basename='cities')


urlpatterns = [
    path('', include(router.urls)),
    path('calculatorpost/', OfferPostApiView.as_view(), name='calculatorpost'),
    path("register/", UserRegisterationAPIView.as_view(), name="create-user"),
    path("login/", UserLoginAPIView.as_view(), name="login-user"),
    path("logout/", UserLogoutAPIView.as_view(), name="logout-user"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
