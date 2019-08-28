from rest_framework import serializers
from providers.models import Provider
from providers.models import Language
from providers.models import Currency


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ['code', 'name']
        read_only_fields = ['code', 'name']
        http_method_names = ['get']


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = ['symbol']
        read_only_fields = ['symbol']
        http_method_names = ['get']


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ['name', 'email', 'phonenumber', 'language', 'currency']
