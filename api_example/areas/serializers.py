from rest_framework import serializers
from areas.models import Area


class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = ['name', 'provider', 'price', 'polygon']
