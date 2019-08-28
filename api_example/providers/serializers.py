from rest_framework import serializers
from providers.models import Provider
from providers.models import Language
from providers.models import Currency


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'code', 'name']
        read_only_fields = ['id', 'code', 'name']
        http_method_names = ['get']


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'symbol']
        read_only_fields = ['id', 'symbol']
        http_method_names = ['get']


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'name', 'email', 'phonenumber', 'language', 'currency']
