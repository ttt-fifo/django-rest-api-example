from rest_framework import viewsets
from providers.serializers import ProviderSerializer
from providers.serializers import LanguageSerializer
from providers.serializers import CurrencySerializer
from providers.models import Provider
from providers.models import Language
from providers.models import Currency


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all().order_by('code')
    serializer_class = LanguageSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all().order_by('symbol')
    serializer_class = CurrencySerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all().order_by('name')
    serializer_class = ProviderSerializer
