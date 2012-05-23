from django.contrib.gis.db import models

class GeographicShape(models.Model):
    """
    A simple ABC for storing geographic shapes, e.g., polygons.
    """
    name                    = models.CharField(max_length=255)
    administrative_level    = models.IntegerField()
    administrative_type     = models.CharField(max_length=255)
    area                    = models.FloatField()
    area_description        = models.CharField(max_length=255)
    fips                    = models.CharField(max_length=255)

    poly            = models.PolygonField(srid=4326)

    objects         = models.GeoManager()

    class Meta:
        abstract = True

class GeographicEvent(models.Model):
    """
    A simple ABC for storing geographically-linked events.
    """
    name                    = models.CharField(max_length=255)
    start_date_time         = models.DateTimeField()
    end_date_time           = models.DateTimeField()
    point                   = models.PointField()

    related_geographies     = models.ManyToManyField(GeographicShape)

    objects         = models.GeoManager()

    class Meta:
        abstract = True