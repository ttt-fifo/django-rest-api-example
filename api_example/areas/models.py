from django.db import models
from providers.models import Provider
import json
from django.core.exceptions import ValidationError
# from shapely.wkt import loads as geoloads
# from shapely.wkt import dumps as geodumps


class PolygonField(models.CharField):

    description = "Polygon Area Field"

    def get_db_prep_value(self, value, *args, **kwargs):
        if value is None:
            return None
        return json.dumps(value)

    def to_python(self, value):
        if value is None:
            return value
        try:
            return json.loads(value)
        except Exception as e:
            raise ValidationError(str(e))

    def from_db_value(self, value, expression, connection, context):
        return self.to_python(value)

    def formfield(self, **kwargs):
        from django.forms import FloatField
        defaults = {'form_class': FloatField}
        defaults.update(kwargs)
        return super(PolygonField, self).formfield(**defaults)


class Area(models.Model):
    name = models.CharField(max_length=50, blank=False)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE,
                                 blank=False)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=False)
    polygon = PolygonField(max_length=500, blank=False)

    def __str__(self):
        return f'{self.name}'
