from rest_framework import viewsets
from areas.serializers import AreaSerializer
from areas.models import Area


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all().order_by('name')
    serializer_class = AreaSerializer
