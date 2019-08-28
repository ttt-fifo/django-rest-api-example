from rest_framework import serializers
from areas.models import Area


class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = ['id', 'name', 'provider', 'price', 'polygon']
        read_only_fields = ['id']
