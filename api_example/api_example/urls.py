"""
API Example URL routing
"""
from django.urls import include, path
from rest_framework import routers
from providers.views import ProviderViewSet, LanguageViewSet, CurrencyViewSet
from areas.views import AreaViewSet
from geoprices.views import GeopriceViewSet

router = routers.DefaultRouter()
router.register(r'providers', ProviderViewSet)
router.register(r'languages', LanguageViewSet)
router.register(r'currencies', CurrencyViewSet)
router.register(r'areas', AreaViewSet)
router.register(r'geoprices', GeopriceViewSet, basename='geoprice')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/',
         include('rest_framework.urls', namespace='rest_framework')),
    ]
