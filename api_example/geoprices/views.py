from rest_framework import viewsets
from rest_framework.response import Response
from shapely.geometry import Point
from shapely.wkt import loads as geoloads
from areas.models import Area


class GeopriceViewSet(viewsets.ViewSet):
    """
    Model-less viewset (application with non-model endpoint)
    Defines just list model (see documentation for other models posibility)
    """

    def list(self, request):
        """
        Get method
        Query parameters lat, lon
        """

        # get latitude, longitude
        lat = request.query_params.get("lat", None)
        lon = request.query_params.get("lon", None)
        if not lat or not lon:
            return Response([])
        lat = float(lat)
        lon = float(lon)

        # get information for hyperlinked relations
        host = request.get_host()
        scheme = request.scheme

        # construct shapely point
        point = Point(lat, lon)

        # query each polygon and compare if the polygon contains the point
        # (very slow implementation, not suitable for live project)
        # in a live project this should be implemented with a geospatial db:
        # - spatialite (sqlite with spatial extension)
        # - postgis (postgresql gis)
        # - mysql with gis extensions
        # note2: shapely does not have projection.
        # therefore not suitable for live project - projection logic should be
        # added.
        queryset = Area.objects.all()
        result = []
        for area in queryset:
            # loads polygon from string
            polygon = geoloads(area.polygon)

            # checks if polygon contains the point
            if polygon.contains(point):
                result.append(dict(area=f'{scheme}://{host}/areas/{area.id}'))

        return Response(result)
