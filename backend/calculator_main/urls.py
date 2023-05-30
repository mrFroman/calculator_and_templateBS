from django.urls import path, include
from rest_framework import routers, request
from .views import OfferApiView, ListAllUrlsApiView, CitiesTemplateApiView

router = routers.DefaultRouter()
router.register(r'calculator', OfferApiView, basename='calculator')
router.register(r'postdate', ListAllUrlsApiView, basename='postdate')
router.register(r'cities', CitiesTemplateApiView, basename='cities')


urlpatterns = [
    path('', include(router.urls)),
    #path(r'postdate', OfferPostApiView.as_view())
]

