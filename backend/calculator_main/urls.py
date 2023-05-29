from django.urls import path, include
from rest_framework import routers, request
from .views import OfferApiView, OfferPostApiView

router = routers.DefaultRouter()
router.register(r'calculator', OfferApiView, basename='calculator')
#router.register(r'postdate', CategoryApiView, basename='postdate')

urlpatterns = [
    path('', include(router.urls)),
    #path(r'postdate', OfferPostApiView.as_view())
]

