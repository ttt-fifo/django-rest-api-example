from django.db import models
from providers.models import Provider
from django.core.exceptions import ValidationError
from shapely.geometry import Polygon
from shapely.wkt import loads as geoloads


class PolygonField(models.CharField):

    description = "Polygon Area Field"

    def get_db_prep_value(self, value, *args, **kwargs):
        if value is None:
            return None

        try:
            polygon = geoloads(value)
            if not isinstance(polygon, Polygon):
                raise ValidationError("Incorrect Polygon Data")
            elif not polygon.is_valid:
                raise ValidationError("Incorrect Polygon Data")
            return value
        except Exception as e:
            raise ValidationError(f"Incorrect Polygon Data: {e}")


class Area(models.Model):
    name = models.CharField(max_length=50, blank=False)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE,
                                 blank=False)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=False)
    polygon = PolygonField(max_length=500, blank=False)

    def __str__(self):
        return f'[{self.id}] {self.name}'
