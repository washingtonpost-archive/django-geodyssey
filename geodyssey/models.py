from django.contrib.gis.db import models

class GeographicShape(models.Model):
    """
    A simple ABC for storing geographic shapes, e.g., polygons.
    """
    name                    = models.CharField(max_length=255)
    administrative_level    = models.IntegerField(blank=True, null=True)
    administrative_type     = models.CharField(max_length=255, blank=True, null=True)
    area                    = models.FloatField(blank=True, null=True)
    area_description        = models.CharField(max_length=255, blank=True, null=True)
    fips                    = models.CharField(max_length=255, blank=True, null=True)
    poly                    = models.MultiPolygonField(srid=4326)
    objects                 = models.GeoManager()

    class Meta:
        abstract = True

class GeographicEvent(models.Model):
    """
    A simple ABC for storing geographically-linked events.
    """
    name                    = models.CharField(max_length=255)
    start_date_time         = models.DateTimeField()
    end_date_time           = models.DateTimeField(blank=True, null=True)
    point                   = models.PointField(blank=True, null=True)
    objects                 = models.GeoManager()

    class Meta:
        abstract = True