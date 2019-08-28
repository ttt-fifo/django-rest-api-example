from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from geoprices.views import GeopriceGet

urlpatterns = patterns('',
                       url(r'^/$', GeopriceGet.as_view()))
urlpatterns = format_suffix_patterns(urlpatterns)
