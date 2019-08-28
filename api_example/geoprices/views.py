from rest_framework import viewsets
from rest_framework.response import Response
from shapely.geometry import Point
from shapely.wkt import loads as geoloads
from areas.models import Area


class GeopriceViewSet(viewsets.ViewSet):

    def list(self, request):
        lat = request.query_params.get("lat", None)
        lon = request.query_params.get("lon", None)
        if not lat or not lon:
            return Response([])
        lat = float(lat)
        lon = float(lon)

        host = request.get_host()
        scheme = request.scheme

        point = Point(lat, lon)
        queryset = Area.objects.all()
        result = []
        for area in queryset:
            polygon = geoloads(area.polygon)
            if polygon.contains(point):
                result.append(dict(area=f'{scheme}://{host}/areas/{area.id}'))

        return Response(result)
