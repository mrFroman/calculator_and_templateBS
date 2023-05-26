from rest_framework import routers
from .views import OfferApiView


router = routers.DefaultRouter()
router.register(r'calculator', OfferApiView, basename='calculator')

urlpatterns = router.urls

